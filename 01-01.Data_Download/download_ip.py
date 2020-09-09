# API로 접근해서 결과 출력
import urllib.request
# 데이터 읽어 들이기/data에 저장
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()
# 바이너리를 문자열로 변환하여 출력
text = data.decode("utf-8")
print(text)