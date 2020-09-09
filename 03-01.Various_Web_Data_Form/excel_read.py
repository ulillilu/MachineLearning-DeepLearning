import openpyxl 

filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)
# 맨 앞의 시트 추출
sheet = book.worksheets[0]
# 시트의 각 행을 순서대로 추출
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[10].value
    ])
# 필요없는 줄(헤더, 연도, 계) 제거
del data[0]
del data[1]
del data[2]
# 데이터를 인구 순서로 정렬
data = sorted(data, key=lambda x:x[1])
# 하위 10위를 출력
for i, a in enumerate(data):
    if (i >= 7): break
    print(i+1, a[0], int(a[1]))