import openpyxl 

filename = "stats_104102.xlsx"
book = openpyxl.load_workbook(filename)
# 시트 추출
sheet = book.active

for i in range(0, 10):
    total = int(sheet[str(chr(i + 66)) + "3"].value)
    seoul = int(sheet[str(chr(i + 66)) + "4"].value)
    output = total - seoul
    print("서울 제외 인구 =", output)
    
    sheet[str(chr(i + 66)) + "21"] = output
    cell = sheet[str(chr(i + 66)) + "21"]
    
    cell.font = openpyxl.styles.Font(size=14,color="FF0000")
    cell.number_format = cell.number_format
# 엑셀 파일 저장
filename = "population.xlsx"
book.save(filename)
print("ok")