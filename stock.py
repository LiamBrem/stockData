import yfinance as yf

class Stock:

    name = None
    price = None

    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price