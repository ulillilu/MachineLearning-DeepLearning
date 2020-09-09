import MySQLdb
from flask import Flask
import MySQLdb.connections
# MySQLdb._exceptions.OperationalError: (2059, <NULL>) 오류 해결법(사용자 재지정)
# DB new user 생성법:CREATE USER '유저명'@'localhost'IDENTIFIED WITH mysql_native_password BY '비밀번호';
# DB 권한 이양:GRANT ALL PRIVILEGES ON 데이터베이스명.*to 유저명@'localhost';
# DB 연결
conn = MySQLdb.connect(
    user='vpdlzm2',
    passwd='6895',
    host='localhost',
    database='test01')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
    ''')

data = [('Banana', 300),('Mango', 640), ('Kiwi', 280)]
for i in data:
    cur.execute("INSERT INTO items(name,price) VALUES(%s,%s)", i)

cur.execute("SELECT * FROM items")
for row in cur.fetchall():
    print(row)