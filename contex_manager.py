from __init__ import USERS_JSON_PATH, BOOKS_CSV_PATH
import json
import csv

class UserBook:
    def users_json_reader(self):
        """"Read data from JSON file"""
        with open(USERS_JSON_PATH, "r") as users:
            json_reader = json.load(users)
            for user in json_reader:
                yield user

    def books_csv_reader(self):
        """Read data from CSV file"""
        with open(BOOKS_CSV_PATH, "r") as books:
            csv_reader = csv.reader(books)
            next(csv_reader)
            for row in csv_reader:
                yield row

    def output_json_writer(self, result):
        """Write data to JSON file"""
        with open("result.json", "w") as users_books:
            json.dump(result, users_books, indent=4)
