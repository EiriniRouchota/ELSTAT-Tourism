import matplotlib.pyplot as plt
import xlrd as rd
import csv


wb2011 = rd.open_workbook("2011.xls")
wb2012 = rd.open_workbook("2012.xls")
wb2013 = rd.open_workbook("2013.xls")
wb2014 = rd.open_workbook("2014.xls")

data_sheet2011 = wb2011.sheet_by_index(-1)
data_sheet2012 = wb2012.sheet_by_index(-1)
data_sheet2013 = wb2013.sheet_by_index(-1)
data_sheet2014 = wb2014.sheet_by_index(-1)

means_of_transport = ['air','railway','sea','road' ]
print(means_of_transport)

transport_2011=[]
transport_2012=[]
transport_2013=[]
transport_2014=[]

for i in range(2,6):
    transport_2011.append(round(data_sheet2011.cell_value(-2, i)))
    transport_2012.append(round(data_sheet2012.cell_value(-2, i)))
    transport_2013.append(round(data_sheet2013.cell_value(-4, i)))
    transport_2014.append(round(data_sheet2014.cell_value(-4, i)))

total_data_for_transport=[]
for i in range(len(means_of_transport)):
    total_data_for_transport.append(transport_2011[i]+transport_2012[i]+transport_2013[i]+transport_2014[i])

print(transport_2011)
print(transport_2012)
print(transport_2013)
print(transport_2014)
print(total_data_for_transport)

plt.yticks(total_data_for_transport)
plt.bar(means_of_transport,total_data_for_transport)
plt.yscale('log')
plt.ylabel("Αξίξεις")
plt.xlabel("Μέσα μεταφοράς για τη τετραετία 2011-2014")
plt.savefig('zhtoumeno3.png')
plt.show()

data3 = [[means_of_transport], [total_data_for_transport]]
print(means_of_transport)
print(total_data_for_transport)
