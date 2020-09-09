#이미지 데이터 추출하기
import requests
#추출하고자 하는 이미지의 주소를 입력 
r = requests.get("https://i.ytimg.com/an_webp/x8CVBae89V8/mqdefault_6s.webp?du=3000&sqp=CPPy-_kF&rs=AOn4CLCepAeubeWE71wanfJ6JK1quMkwHw")

with open("test.png", "wb") as f:
    f.write(r.content)
print("saved")