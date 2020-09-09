#환율 정보 추출
from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")
#div.class명(일부만 입력해도 됨)
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)