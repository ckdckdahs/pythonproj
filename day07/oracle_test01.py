#pip install cx_Oraacle

import cx_Oracle

conn = cx_Oracle.connect('scott','tiger','localhost:1521/XE')
cursor = conn.cursor()
cursor.execute("select * from emp where deptno = 10")

# print(cursor)

# for item in cursor:
#     while True:
#         job = input('직업을 입력하세요 >>> ').upper()
#         if job in item[2]:
#             print(item[1])
#             break
#         else:
#             print('직업을 정확히 입력해주세요.')

for item in cursor:
    print(item[1],item[5])
# for item in cursor:
#     print(item[1])


conn.close()