
import csv
hosts = [["workstation.local","192.168.122.1"] , ["webserver.cloud","192.168.122.1"]]
with open('hosts.csv' , 'w') as hosts_csv:
    writer = csv.writer(hosts_csv) #  writer function to generate contents to a file
    writer.writerows(hosts) # using writerows method to write data in row form