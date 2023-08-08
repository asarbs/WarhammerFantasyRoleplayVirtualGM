#!/usr/bin/env python3

import csv

print("[")
with open("class_1.csv", "r") as csvfile:
    class_reader = csv.DictReader(csvfile, delimiter=",")
    for row in class_reader:
        print(row)
        print(",")

print("]")