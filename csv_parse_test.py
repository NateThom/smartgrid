import csv
dataReader = csv.reader(open('household_power_consumption.txt', newline='\n'), delimiter=';', quotechar='|')
for row in dataReader:
    date = row[0]
    time = row[1]
    voltage = row[4]

    print(date)
    for character in date:
