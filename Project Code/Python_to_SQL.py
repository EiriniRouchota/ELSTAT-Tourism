import xlrd as rd
import csv
import zhtoumeno1
import zhtoumeno2
import zhtoumeno4
import zhtoumeno3
import sqlite3

conn = sqlite3.connect('SQLite.db')
c = conn.cursor()
xa = zhtoumeno1.xAxis
val = zhtoumeno1.values
tc = zhtoumeno2.topCountries
mv = zhtoumeno2.max_values
transport = zhtoumeno3.total_data_for_transport
xax = zhtoumeno4.xaxis
sem= zhtoumeno4.semesters


# create table
c.execute('''CREATE TABLE IF NOT EXISTS arrivals_by_year
             (year int, arrivals int)''')
c.execute('''CREATE TABLE IF NOT EXISTS top10
             (country text, arrivals)''')
c.execute('''CREATE TABLE IF NOT EXISTS entrance_type
             (air int,railway int,sea int, road int)''')
c.execute('''CREATE TABLE IF NOT EXISTS semesters_data
             (semester int , arrivals int )''')

for i in range(len(tc)):
    de = [tc[i], mv[i]]
    tup = tuple(de)
    stmt = "INSERT INTO top10 VALUES(?,?)"
    c.executemany(stmt,[tup])
    #print(tuple(de))
for i in range(len(xa)):
    de = [xa[i], val[i]]
    tup = tuple(de)
    stmt = "INSERT INTO arrivals_by_year VALUES(?,?)"
    c.executemany(stmt,[tup])
    #print(tuple(de))
for i in range(0,1):
    de = [transport[i], transport[i+1],transport[i+2],transport[i+3]]
    tup = tuple(de)
    stmt = "INSERT INTO entrance_type VALUES(?,?,?,?)"
    c.executemany(stmt,[tup])
    #print(tuple(de))
for i in range(len(xax)):
    de = [xax[i],sem[i]]
    tup = tuple(de)
    stmt = "INSERT INTO semesters_data VALUES(?,?)"
    c.executemany(stmt,[tup])
    #print(tuple(de))



# commit the changes to db
conn.commit()
# close the connection
conn.close()