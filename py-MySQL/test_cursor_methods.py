import pymysql as sql

conn = sql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root',
    db = 'imooc',
    charset = 'utf8'
)

cursor = conn.cursor()

sql = "select * from user2"
cursor.execute(sql)

print(cursor.rowcount)

rs = cursor.fetchone()
print(rs)

rs = cursor.fetchmany(3)
print(rs)

rs = cursor.fetchall()
print(rs)

for row in rs:
    print("userid=%s,username=%s" %row)
    print(row)


cursor.close()
conn.close()