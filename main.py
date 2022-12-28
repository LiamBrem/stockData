import PySimpleGUI as sg
from stock import Stock

sg.theme('darkAmber')

stockList = [Stock("AAPL", 40), Stock("GOOGL", 30),
             Stock("TSLA", 20), Stock("AMZN", 10)]

# takes the list of stock objects and returns a list of just the string values of their symbol
def convertObjectToString(listOfStockObjects):
    newList = []
    for stock in listOfStockObjects:
        newList.append(stock.symbol)
    return newList

stockListStrings = convertObjectToString(stockList)

layoutHeader = [
    [sg.Text("Symbol"), sg.Input(key="-INPUT-"), sg.Button("ADD STOCK")]
]

listOfStocks = [
    [sg.Listbox(values=stockListStrings, size=(
        40, 10), key="items"), sg.Button('More Info'), sg.Button("Remove")]
]

leftColumn = [layoutHeader, listOfStocks]

layout = [
    layoutHeader,
    listOfStocks
]
window = sg.Window("Program", layout, margins=(150, 200))


# Main Event Loop

while True:
    event, values = window.read()
    print(event, values)

    if event == "ADD STOCK":
        stock = Stock(values["-INPUT-"], 50)

        stockList.append(stock)
        stockListStrings = convertObjectToString(stockList)
        window["items"].Update(values=stockListStrings)
    if event == "Remove":
        index = stockListStrings.index(values["items"][0])
        stockListStrings.remove(values["items"][0])
        stockList.pop(index)
        window["items"].Update(values=stockListStrings)
    if event == "More Info":
        pass
    if event == sg.WIN_CLOSED:
        break

window.close()
