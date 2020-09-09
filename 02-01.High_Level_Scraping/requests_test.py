# 데이터 가져오기
import requests
r = requests.get("http://api.aoikujira.com/time/get.php")

text = r.text
print(text)

bin = r.content
print(bin)