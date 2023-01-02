import yfinance as yf
import matplotlib.pyplot as plt

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price

        self.tickerObj = yf.Ticker(symbol)

    def symbolHistory(self):
        return self.tickerObj.history(period="1mo", interval="1d")

    def drawGraph(self):
        pass


#example = Stock("AAPL", 4747)

#print(example.symbolHistory())

#print(example)