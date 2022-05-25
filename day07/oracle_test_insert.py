from datetime import datetime as d
import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()

sql = "insert into fruit values(:1,:2,:3,:4)"

sql2 = "select * from price"
bill = cursor.execute(sql2)

print('----- <과일 목록> -----')
for item in bill :
    print(item[0])
print('-----------------------')
name1 = input('과일명 >>> ')

stock1 = int(input('입고량 >>> '))
come = d.now().date()  #현재 날짜

sql3 = "select * from loc"
locate = cursor.execute(sql3)

print('------ <원산지> ------')
for item1 in locate :
    print(item1)
print('----------------------')
loc_num = int(input('원산지번호 >>> '))

data = (name1, stock1, come, loc_num)
cursor.execute(sql,data)
cursor.close()
conn.commit()
conn.close()