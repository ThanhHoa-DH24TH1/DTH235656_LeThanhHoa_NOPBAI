import csv
with open('datacsv.csv', newline='',encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row[0],"-",row[1])