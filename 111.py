import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# cursor.execute("drop table test")
cursor.execute('''create table fruit(
num1 number(4) constraint num_p primary key,
name1 varchar2(20) constraint name_f references price(name1),
stock1 number(3), 
come date,
die date,
loc_num number(3) constraint loc_f references loc(loc_num)
)''')
#cursor.execute("insert into ")
cursor.close()
conn.commit()
conn.close()

import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# cursor.execute("drop table test")
cursor.execute('''create table price(
name1 varchar2(20) constraint name_p primary key,
price1 number(5) constraint price_c check (price1 between 500 and 50000)
)''')
#cursor.execute("insert into ")
 
cursor.close()
conn.commit()
conn.close()


import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
# cursor.execute("drop table test")
cursor.execute('''create table loc (
loc_num number(3) constraint loc_p primary key,
loc1 varchar2(10)
);''')
#cursor.execute("insert into ")
cursor.close()
conn.commit()
conn.close()