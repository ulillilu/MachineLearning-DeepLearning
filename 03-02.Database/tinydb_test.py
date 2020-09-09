from tinydb import TinyDB, Query

filepath = "test-tinydb.json"
db = TinyDB(filepath)
# 기존의 테이블이 있다면 제거
#db.purge_table('fruits')
# 테이블 생성/추출
table = db.table('fruits')
# 테이블에 데이터 추가
table.insert( {'name': 'Banana', 'price': 6000} )
table.insert( {'name': 'Orange', 'price': 12000} )
table.insert( {'name': 'Mango', 'price': 8400} )
# 모든 데이터를 추출해서 출력
print(table.all())
# 특정 데이터 추출
Item = Query()
res = table.search(Item.name == 'Orange')
print('Orange is ', res[0]['price'])

print("8000원 이상인 것:")
res = table.search(Item.price >= 8000)
for it in res:
    print("-", it['name'])