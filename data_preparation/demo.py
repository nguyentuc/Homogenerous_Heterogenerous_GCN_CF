import csv

with open("data/new_data", "r") as f:
    csv_reader = csv.reader(f, delimiter=",", quotechar="", quoting=csv.QUOTE_NONE)