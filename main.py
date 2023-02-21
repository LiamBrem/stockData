import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib import style


def graph(x, y1, y2):
  #dark mode
  plt.style.use('dark_background')
  
  plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
  plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=750))


  fig, ax1 = plt.subplots();
  
  
  ax1.plot(x, y1, 'c-')
  ax1.set_xlabel('Date')
  ax1.set_ylabel('Stock Price', color='c')

  # Create the second plot with the right y-axis
  ax2 = ax1.twinx()
  ax2.plot(x, y2, 'm-')
  ax2.set_ylabel('Market Trends', color='m')
  
  plt.show()


def getStartEnd():
  end = datetime.date.today()
  start = end.replace(year=end.year - 10)
  return start, end


def getXPoints(stockSymbol):
  x = []

  start, end = getStartEnd()

  symbol_ticker = yf.Ticker(stockSymbol)

  history = symbol_ticker.history(start=start, end=end)

   #list of dates
  sf = history["Close"]
  df = pd.DataFrame({'Date': sf.index, 'Values': sf.values})

  #list of corresponding dates
  listOfDateTimes = df['Date'].tolist()
  listOfDates = []

  for i in listOfDateTimes:
    date = str(i)
    date = date[0:10]

    listOfDates.append(date)

  #converts yyyy-mm-dd to yyyy/mm/dd
  for i in range(len(listOfDates)):
    iList = list(listOfDates[i])
    for j in range(len(iList)):
      if iList[j] == "-":
        iList[j] = "/"
    listOfDates[i] = ''.join(iList)

  #this must be in mm/dd/yyyy
  for i in range(len(listOfDates)):
    #converts value to list
    iList = list(listOfDates[i])
    #appends /
    iList.append("/")
    #appends first 4 characters
    for j in range(0, 4):
      iList.append(iList[j])
    #makes the list every character except the first 5
    iList = iList[5:]

    listOfDates[i] = ''.join(iList)

  x = [datetime.datetime.strptime(d, '%m/%d/%Y').date() for d in listOfDates]

  #print(x)
  return x


def getYPoints(stockSymbol):
  y = []

  start, end = getStartEnd()

  symbol_ticker = yf.Ticker(stockSymbol)

  history = symbol_ticker.history(start=start, end=end)

  #gets the closing value every day
  for i in range(len(history)):
    y.append(history["Close"][i])

  #print(y)
  return y


def graphCluster(symbol):
  start, end = getStartEnd()
  symbol_ticker = yf.Ticker(symbol)
  df = symbol_ticker.history(start=start, end=end)

  mpl.rc('figure', figsize=(8, 7))
  mpl.__version__

  # Adjusting the style of matplotlib
  style.use('dark_background')
  
  close_px = df['Close']

  #moving average
  #mavg = close_px.rolling(window=100).mean()

  #returns 
  #rets = close_px / close_px.shift(1) - 1

  compareStock = input("What stock would you like to display the correlation with?: ")

  spTicker = yf.Ticker(compareStock)
  spdf = spTicker.history(start=start, end=end)

  data = []

  for i in range(len(df["Close"])):
    listToAppend = []
    listToAppend.append(df["Close"][i])
    listToAppend.append(spdf["Close"][i])
    data.append(listToAppend)


  combinedDf = pd.DataFrame(data, columns=["STOCK1", "STOCK2"])

  #percentage change
  retscomp = combinedDf.pct_change()

  corr = retscomp.corr()

  plt.scatter(retscomp.STOCK1, retscomp.STOCK2, color="m")
  plt.xlabel(symbol + " Returns")
  plt.ylabel(compareStock + " S&P Returns")

  plt.show()
  


if __name__ == "__main__":
  print("this program compares any stock to the overall S&P 500")
  symbol = input("Enter the symbol you want to use: ")

  option = input("(1) Linear Comparison\n(2) Cluster Analysis\n")
  if option == "1":
    xpoints = getXPoints(symbol)
    ypoints = getYPoints(symbol)
    sppoints = getYPoints("^GSPC")
  
    graph(xpoints, ypoints, sppoints)
    
    print("Close the first window to see the graph")
    print("CTRL+C to quit")
  elif option == "2":
    graphCluster(symbol)
