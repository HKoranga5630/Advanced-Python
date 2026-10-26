import csv
import json

# Read data from the CSV file
with open("Unit3/input.csv", "r", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    data = list(reader)

# Write data to the JSON file
with open("Unit3/output.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("CSV data successfully converted to JSON!")
print("Output saved in output.json")