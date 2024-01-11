import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta
import numpy as np


def add_period(original_date, add_amount):
    future_date = original_date + relativedelta(months=add_amount)
    if future_date > datetime.now():
        future_date = datetime.now()
    return future_date

def check_investment(ticker, buy, transaction_date, period_tolerance, price_tolerance):
    stock = yf.Ticker(ticker)
    future_date = add_period(transaction_date, period_tolerance)

    try:
        period_data = list(stock.history(start=transaction_date, end=future_date)["Close"])
        average_price = np.mean(period_data)
        starting_price = period_data[0]

        print(f"{starting_price} -> {average_price} : {'Bought' if buy else 'Sold'}")
        
        if buy and average_price >= starting_price * (1 + price_tolerance):
            return True

        elif not buy and average_price <= starting_price * (1 - price_tolerance):
            return True
        
    except IndexError:
        print("Error!")
    
    return False

def get_info(ticker, *info_tags):    
    stock = yf.Ticker(ticker)
    
    try:
        stock_info = stock.info
    except:
        raise ValueError("404 Error, Info not found")

    return_values = []
    for tag in info_tags:
        try:
            return_values.append(stock_info[tag])
        except:

            return_values.append(False)


    return tuple(return_values)
        


if __name__ == '__main__':
    print(get_info("TSLA", "industry"))
