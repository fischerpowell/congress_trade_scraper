import json
from stock_checker import check_investment
from datetime import datetime


with open("congress_trading_dataset.json", "r") as f:
    dataset = json.load(f)


scoreboard = {}


record_count = 1000

counter = 0

winner_amount = 10


for record in dataset:
    print('----------')


    if record["Transaction Type"] == "Purchase":
        bought = True
    else:
        bought = False

    formatted_date = datetime.strptime(record['Transaction Date'], "%m/%d/%Y")

    congressperson = record["Office (Filer Type)"]

    if check_investment(record["Ticker"], bought, formatted_date, 12, .01):

        print("Good investment")

        try:
            scoreboard[congressperson] += 1
        except:
            scoreboard[congressperson] = 1
    else:
        print("Bad investment")
        try:
            scoreboard[congressperson] -= 1
        except:
            scoreboard[congressperson] = -1

    print(f"{congressperson}: {scoreboard[congressperson]}")
    counter += 1

    if counter > record_count:
        break



print(f"Congress's Top {winner_amount} Winners:")

for i in range(winner_amount):
    winner = max(scoreboard, key=scoreboard.get)
    print(f"{winner}: {scoreboard[winner]}")
    del scoreboard[winner]

    if not scoreboard:
        break

print(f"Congress's Top {winner_amount} Losers:")
for i in range(winner_amount):
    winner = min(scoreboard, key=scoreboard.get)
    print(f"{winner}: {scoreboard[winner]}")
    del scoreboard[winner]

    if not scoreboard:
        break