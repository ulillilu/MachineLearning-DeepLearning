import requests
import json

apikey = "a30634c689a6e2645eb3d0b4dafa164a"

cities = ["Seoul,KR", "Tokyo,JP", "New York,US", "London,UK"]

api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
# 켈빈 온도를 섭씨 온도로 변환하는 함수
k2c = lambda k: k - 273.15

for name in cities:   
    url = api.format(city=name, key=apikey)
    print(url)
    # 데이터 추출
    r = requests.get(url)
    # 결과를 JSON 형식으로 변환
    data = json.loads(r.text)  
    # 결과 출력
    print("+ 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
    print("")