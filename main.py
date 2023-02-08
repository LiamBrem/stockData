import yfinance as yf
import datetime



def graph():
    pass

def getStartEnd():
    end = datetime.date.today()
    start = end.replace(year=end.year-10)

    print(start)
    print(end)

    return start,end

def getPoints(symbol):
    x = []
    y = []

    start,end = getStartEnd()


    symbol_ticker = yf.Ticker(symbol)


    return x,y

if __name__ == "__main__":
    print("this program compares any stock to the overall S&P 500")
    symbol = input("Enter the symbol you want to use: ")

    #xpoints, ypoints = getPoints(symbol)

    getStartEnd()