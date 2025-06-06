#!/usr/bin/python3
import json
import csv


def convert_csv_to_json(filename):
    data = []
    try:
        with open(filename, "r") as f:
            for x in csv.DictReader(f):
                data.append(x)

        with open("data.json", "w") as f:
            json.dump(data)
        return True
    except Exception:
        return False
