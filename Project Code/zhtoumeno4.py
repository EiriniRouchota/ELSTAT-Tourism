import xlrd as rd
import matplotlib.pyplot as plt

wb2011 = rd.open_workbook("2011.xls")
wb2012 = rd.open_workbook("2012.xls")
wb2013 = rd.open_workbook("2013.xls")
wb2014 = rd.open_workbook("2014.xls")

xaxis = [ '1-2011', '2-2011','3-2011', '4-2011','1-2012', '2-2012','3-2012', '4-2012','1-2013', '2-2013','3-2013', '4-2013','1-2014', '2-2014','3-2014', '4-2014']
final = []
semesters = []
for i in range(0,12):
    semester_sheet = wb2011.sheet_by_index(i)
    final.append(round(semester_sheet.cell_value(65, 6)))

for i in range(0,12):
    semester_sheet = wb2012.sheet_by_index(i)
    final.append(round(semester_sheet.cell_value(65, 6)))

for i in range(0,12):
    semester_sheet = wb2013.sheet_by_index(i)
    if i<6:
        final.append(round(semester_sheet.cell_value(64, 6)))
    else:
        final.append(round(semester_sheet.cell_value(65, 6)))

for i in range(0,12):
    semester_sheet = wb2014.sheet_by_index(i)
    final.append(round(semester_sheet.cell_value(65, 6)))

for i in range(0,46,3):
    semesters.append(final[i] + final[i+1] + final[i+2])

print(len(semesters))

plt.bar(xaxis,semesters)
plt.xticks(xaxis)
plt.ylabel("Αφίξεις")
#plt.xlabel("Years")
#plt.savefig('zhtoumeno4.png')
plt.show()
data4 = [xaxis], [semesters]
print(data4)
print(final)





