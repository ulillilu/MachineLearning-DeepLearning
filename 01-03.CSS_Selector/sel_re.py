#정규 표현식과 함께 조합
from bs4 import BeautifulSoup 
import re

html = """
<ul>
  <li><a href="hoge.html">hoge</li>
  <li><a href="https://example.com/fuga">fuga*</li>
  <li><a href="https://example.com/foo">foo*</li>
  <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")
#re의 compile()함수로 정규표현식 생성/https://가 들어가는 것 모두 추출
li = soup.find_all(href=re.compile(r"^https://"))
for e in li: 
  print(e.attrs['href'])