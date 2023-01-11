import yfinance as yf
#import matplotlib.pyplot as plt

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

        self.tickerObj = yf.Ticker(symbol)

    def symbolHistory(self, period, interval):
        return self.tickerObj.history(period=period, interval=interval)

    def drawGraph(self):
        pass

    def recentPerformance(self):
        #take the first value for month and the last value & compare

        history = self.symbolHistory("1m", "1d")


        print(history)


example = Stock("AAPL", 4747)

example.recentPerformance()

#print(example)