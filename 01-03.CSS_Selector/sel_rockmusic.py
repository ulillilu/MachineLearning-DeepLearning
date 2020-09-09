#스크레이핑 기초
from bs4 import BeautifulSoup 
import urllib.request as req

url = "https://ko.wikipedia.org/wiki/%EB%A1%9D_%EC%9D%8C%EC%95%85"
res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")
#copy selector를 통해 쉽게 경로 선택후 Header 경로를 일부 수정해준다(class명에 띄어쓰기가 있는 경우 첫번째 어절만 입력/최대한 간단하게 입력)
a_list = soup.select("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr > td > div > ul > li > a")
for a in a_list:
    name = a.string
    print("-", name)