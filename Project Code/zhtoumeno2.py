import matplotlib.pyplot as plt
import xlrd as rd


wb2011 = rd.open_workbook("2011.xls")
wb2012 = rd.open_workbook("2012.xls")
wb2013 = rd.open_workbook("2013.xls")
wb2014 = rd.open_workbook("2014.xls")

total_arrivals2011 = wb2011.sheet_by_index(-1)
total_arrivals2012 = wb2012.sheet_by_index(-1)
total_arrivals2013 = wb2013.sheet_by_index(-1)
total_arrivals2014 = wb2014.sheet_by_index(-1)

countries = []
arrivals2011 = []
arrivals2012 = []
arrivals2013 = []
arrivals2014 = []

#78-111
for i in range(77,111):
    countries.append(total_arrivals2014.cell_value(i, 1))
    arrivals2014.append(round(total_arrivals2014.cell_value(i, 6)))
    arrivals2013.append(round(total_arrivals2013.cell_value(i, 6)))
    if i == 88:
        arrivals2012.append(0)
        arrivals2011.append(0)
    if i != 110:
        arrivals2012.append(round(total_arrivals2012.cell_value(i+1, 6)))
        arrivals2011.append(round(total_arrivals2011.cell_value(i-1, 6)))

#113-121
for i in range(112,121):
    countries.append(total_arrivals2014.cell_value(i,1))
    arrivals2014.append(round(total_arrivals2014.cell_value(i, 6)))
    arrivals2013.append(round(total_arrivals2013.cell_value(i, 6)))
    arrivals2012.append(round(total_arrivals2012.cell_value(i, 6)))
    arrivals2011.append(round(total_arrivals2011.cell_value(i-2, 6)))

#123-125
for i in range(122,125):
    countries.append(total_arrivals2014.cell_value(i,1))
    arrivals2014.append(round(total_arrivals2014.cell_value(i, 6)))
    arrivals2013.append(round(total_arrivals2013.cell_value(i, 6)))
    arrivals2012.append(round(total_arrivals2012.cell_value(i, 6)))
    arrivals2011.append(round(total_arrivals2011.cell_value(i-2, 6)))

#127-132
for i in range(126,132):
    countries.append(total_arrivals2014.cell_value(i,1))
    arrivals2014.append(round(total_arrivals2014.cell_value(i, 6)))
    arrivals2013.append(round(total_arrivals2013.cell_value(i, 6)))
    arrivals2012.append(round(total_arrivals2012.cell_value(i, 6)))
    arrivals2011.append(round(total_arrivals2011.cell_value(i-2, 6)))

#134-135
for i in range(133,135):
    countries.append(total_arrivals2014.cell_value(i,1))
    arrivals2014.append(round(total_arrivals2014.cell_value(i, 6)))
    arrivals2013.append(round(total_arrivals2013.cell_value(i, 6)))
    arrivals2012.append(round(total_arrivals2012.cell_value(i, 6)))
    arrivals2011.append(round(total_arrivals2011.cell_value(i-2, 6)))

total_arrival_year = []

for i in range(len(countries)):
    total_arrival_year.append(arrivals2011[i] + arrivals2012[i] + arrivals2013[i] + arrivals2014[i])

index = []
max_values = []
topCountries = []
for i in range (10):
    maximum = max(total_arrival_year)
    index.append(total_arrival_year.index(maximum))
    max_values.append(maximum)
    total_arrival_year[index[i]] = -1
    topCountries.append(countries[index[i]])

print(max_values)
print(index)


plt.barh(topCountries,max_values)
plt.ylabel("Total arrivals")
plt.xlabel("Years")
plt.savefig('zhtoumeno2.png')
plt.show()

data2 = topCountries,max_values
print(countries)
print(arrivals2011)