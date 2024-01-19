'''
This code takes in the JSON file of senator trades, removes certain columns, 
saves it as a JSON file, and then aditionally as a CSV without duplicates.
'''
import json
import pandas as pd

with open("congress_trading_dataset.json", "r") as f:
    dataset = json.load(f)

heading_list = ["Office (Filer Type)", "Ticker", "Transaction Type", "Transaction Date", "Amount"]
#Change these as you wish

new_dataset = []

for record in dataset:
    new_record = {}

    for header in heading_list:
        new_record[header] = record[header]


    new_dataset.append(new_record)

with open("slimmed_trading_dataset.json", "w") as new_file:
    json.dump(new_dataset, new_file)


# Opens JSON file
f = open("slimmed_trading_dataset.json")
 
# converts JSON into dictionary 
data = json.load(f)

new_data = pd.DataFrame(data)



new_data.drop_duplicates(inplace=True)
new_data.to_csv("slimmed_trading_dataset.csv", index=False)

