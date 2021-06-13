import csv
import zhtoumeno1
import zhtoumeno2
import zhtoumeno4
import zhtoumeno3


data = zhtoumeno1.data
data2 = zhtoumeno2.data2
data3 = zhtoumeno3.data3
data4 = zhtoumeno4.data4
f = open('final_data.csv', 'w')

with f:
    writer = csv.writer(f)

    for row in data:
        writer.writerow(row)
    for row in data2:
        writer.writerow(row)
    for row in data3:
        writer.writerow(row)
    for row in data4:
        writer.writerow(row)

