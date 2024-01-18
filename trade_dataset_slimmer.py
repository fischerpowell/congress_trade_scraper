import json

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

