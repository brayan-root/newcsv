# each line in a CSV file generally represents a single data record.
# Each field in that record is separated by a comma, with the contents of the field stored between the commas
import csv #module which lets us read, create and manipulate CSV files
file = open("csv_file.txt")
csv_f = csv.reader(file) #The reader() function of the CSV module will interpret the file as a CSV.
for row in csv_f: #we can unpack the values so that we can use variables to refer to them.
    name, phone, role= row #for it to work you should have the same number of values as the field in row variable
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))