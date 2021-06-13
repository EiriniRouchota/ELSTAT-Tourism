import matplotlib.pyplot as plt
import xlrd as rd
import xlwt
import csv

wb2011 = rd.open_workbook("2011.xls")
wb2012 = rd.open_workbook("2012.xls")
wb2013 = rd.open_workbook("2013.xls")
wb2014 = rd.open_workbook("2014.xls")

total_arrivals2011 = wb2011.sheet_by_index(-1)
total_arrivals2012 = wb2012.sheet_by_index(-1)
total_arrivals2013 = wb2013.sheet_by_index(-1)
total_arrivals2014 = wb2014.sheet_by_index(-1)


value2011 = total_arrivals2011.cell_value(-2, 6)
value2012 = total_arrivals2012.cell_value(-2, 6)
value2013 = total_arrivals2013.cell_value(-4, 6)
value2014 = total_arrivals2014.cell_value(-4, 6)


xAxis = range(2011,2015)
plt.bar(xAxis,[value2011,value2012,value2013,value2014])
plt.xticks(xAxis)
plt.ylabel("Total arrivals")
plt.xlabel("Years")
plt.savefig('zhtoumeno1.png')
plt.show()



data=[2011,2012,2013,2014],[value2011,value2012,value2013,value2014]
values = value2011,value2012,value2013,value2014
print(data)


