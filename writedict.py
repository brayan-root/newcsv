import csv
users = [{"name": "judy", "username": "jud", "department": "ICT" },
         {"name": "jane", "username": "jan", "department": "audit" },
         {"name": "james", "username": "jam", "department": "finance" }]
keys = ["name", "username", "department"]
with open('by_department.csv', mode='w') as by_department:
    writer = csv.DictReader(by_department, fieldnames=keys)
    writer.writeheader()  #header method will create the first line of the CSV based on keys that we passed
    writer.writerows() #rows method will turn the list of dictionaries into lines in that file
#The fieldnames parameter of DictWriter() requires a list of keys This will help DictWriter() organize the CSV rows properly.