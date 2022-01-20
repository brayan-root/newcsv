import csv
with open('software.csv') as software: #opens a csv file and closes it
    reader = csv.DictReader(software) #reader turns each row of the data in a CSV file into a dictionary
    for row in reader:
        print(("{} is in {} state").format(row["name"], row["status"] )) #access the data by using the column names instead of the position in the row


