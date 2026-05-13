import pandas as pd
import yfinance

def get_stock_data(ticker, period):
    finace = yfinance.download(ticker,period=period)
    return finace



if __name__ == "__main__":
    df= get_stock_data('AAPL','2Y')
    print(df.head())