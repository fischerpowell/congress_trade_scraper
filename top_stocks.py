import json
from stock_checker import get_info
from datetime import datetime
from dateutil.relativedelta import relativedelta


with open("congress_trading_dataset.json", "r") as f:
    dataset = json.load(f)


ticker_counter = {}

record_count = 20000

counter = 0

winner_amount = 10

period = 12

for record in dataset:

    try:
        formatted_date = datetime.strptime(record['Transaction Date'], "%m/%d/%Y")

        if formatted_date + relativedelta(months=period) >= datetime.now():
            print(formatted_date)
            if record['Transaction Type'] == 'Purchase':
                try:
                    ticker_counter[record['Ticker']] += 1
                except:
                    ticker_counter[record['Ticker']] = 1
    except ValueError:
        pass

    counter += 1

    if counter > record_count:
        break

print(f"Congress's Top {winner_amount} Recent Stocks:")

for i in range(winner_amount):
    winner = max(ticker_counter, key=ticker_counter.get)
    print(f"{winner} / {get_info(winner, 'longName')[0]}: {ticker_counter[winner]}")
    del ticker_counter[winner]


    if not ticker_counter:
        break

