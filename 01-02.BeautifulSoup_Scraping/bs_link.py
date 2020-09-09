#find_all로 여러개의 요소 추출
from bs4 import BeautifulSoup 
html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")
# 링크의 href 속성은 attrs 속성에서 추출
for i in links:
    t_href = i.attrs['href']
    text = i.string
    print(text, ">", t_href)