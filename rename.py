import os
import csv

with open('src.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        name = 'IE ' + row[7] + '.pdf'
        new = row[0] + row[4] + '.pdf'
        if os.path.exists(name):
            os.rename(name, new)
        else:
            print(name + ' does not exist')
