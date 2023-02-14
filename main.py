import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def graph(x,y):
    plt.plot(xpoints, ypoints)
    plt.show()

def getStartEnd():
    end = datetime.date.today()
    start = end.replace(year=end.year-10)
    return start,end

def getPoints(stockSymbol):
    x = []
    y = []

    start,end = getStartEnd()

    symbol_ticker = yf.Ticker(stockSymbol)

    history = symbol_ticker.history(start=start, end=end)

    print(history)

    #list of dates
    sf = history["Close"]
    df = pd.DataFrame({'Date':sf.index, 'Values':sf.values})

    #list of corresponding dates
    listOfDateTimes = df['Date'].tolist()
    listOfDates = []

    for i in range(len(listOfDateTimes)):
        date = str(listOfDateTimes[i])
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
        for j in range(0,4):
            iList.append(iList[j])
        #makes the list every character except the first 5
        iList = iList[5:]
        print(iList)

        listOfDates[i] = ''.join(iList)



    x = [datetime.datetime.strptime(d,'%m/%d/%Y').date() for d in listOfDates]

    #gets the closing value every day
    for i in range(len(history)):
        y.append(history["Close"][i])

    print(x)
    print(y)

    return x,y

if __name__ == "__main__":
    print("this program compares any stock to the overall S&P 500")
    symbol = input("Enter the symbol you want to use: ")

    xpoints, ypoints = getPoints(symbol)


    #graph(xpoints,ypoints)
