import csv
import json

cr = csv.reader(open("ffinput.csv","rb"))

data = ''
for row in cr:
    data += str(row).replace('"', '\"').replace("'",'"') + ",\n"

print data
