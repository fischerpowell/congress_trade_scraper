import json
from stock_checker import get_info
from datetime import datetime


with open("congress_trading_dataset.json", "r") as f:
    dataset = json.load(f)


sector_counter = {}


record_count = 10000

counter = 0

winner_amount = 10


for record in dataset:

    try:
        industry, = get_info(record["Ticker"], "industry")
        
        if not industry:
            industry = "Index"


        try:
            sector_counter[industry] += 1
        except:
            sector_counter[industry] = 1
    except ValueError:
        pass



    counter += 1

    if counter > record_count:
        break



print(f"Congress's Top {winner_amount} Investment Industries:")

for i in range(winner_amount):
    winner = max(sector_counter, key=sector_counter.get)
    print(f"{winner}: {sector_counter[winner]}")
    del sector_counter[winner]

    if not sector_counter:
        break

