import urllib.request
import urllib.parse
API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#매개변수 지정/stnID는 지역번호
values = {
    'stnId': '108'
}
#지역번호를 매개변수를 통해 전달하고 인코딩
params = urllib.parse.urlencode(values)
#접근하고자하는 URL 생성
url = API + "?" + params
print("url=", url)
#URL에 접근하여 데이터 읽어들임
data = urllib.request.urlopen(url).read()
#디코딩하여 출력
text = data.decode("utf-8")
print(text)