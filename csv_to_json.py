import csv
import json

def csv_to_json(csv_file, json_file):
    data = []

    with open(csv_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(json_file, mode='w') as json_out:
        json.dump(data, json_out, indent=4)

    print("✅ CSV successfully converted to JSON")

if __name__ == "__main__":
    csv_input = "test_data.csv"
    json_output = "test_data.json"
    csv_to_json(csv_input, json_output)
