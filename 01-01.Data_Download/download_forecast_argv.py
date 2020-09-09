import sys
import urllib.request as req
import urllib.parse as parse

if len(sys.argv) <= 1:
    #명령줄에 변수를 입력하지 않았을 경우
    print("USAGE: 명령줄에 지역번호를 입력해주세요. <Region Number>")
    sys.exit()
#명령줄에 입력한 변수가 리스트 sys.argv에 저장되고 regionNumber에 저장
regionNumber = sys.argv[1]

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId': regionNumber
}
params = parse.urlencode(values)
url = API + "?" + params
print("url=", url)

data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)