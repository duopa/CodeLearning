import pymysql as sql

conn = sql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = 'root'
)

cursor = conn.cursor()

print(conn)
print(cursor)