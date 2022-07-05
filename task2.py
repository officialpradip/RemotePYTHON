'''write program to read csv file and create list of dict'''

import csv

filename = "pradip.csv"

with open(filename, 'r') as f:
    for line in csv.reader(f):
        print(line)


# for creating list of dictionary
filename = "pradip.csv"


with open(filename, 'r') as f:

    for line in csv.DictReader(f):
        print(line)
