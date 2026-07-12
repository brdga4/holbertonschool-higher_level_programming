import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            csv_data = csv.DictReader(file)

            data_list = []
            for row in csv_data:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file, indent=4)
        return True
    except (FileNotFoundError, EOFError):
        return False
