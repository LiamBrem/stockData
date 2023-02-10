import yfinance as yf
import datetime
import matplotlib.pyplot as plt
import numpy as np



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

    for i in range(len(history)):
        #this date may have to be changed
        print(history["Date"][i])

        #x.append(history["Date"][i])
        y.append(history["Close"][i])

    return x,y

if __name__ == "__main__":
    print("this program compares any stock to the overall S&P 500")
    symbol = input("Enter the symbol you want to use: ")

    xpoints, ypoints = getPoints(symbol)


    #graph(xpoints,ypoints)
