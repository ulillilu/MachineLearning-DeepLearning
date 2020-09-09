#CSS 선택자 사용하기
from bs4 import BeautifulSoup 

html = """
<html><body>
<div id="meigen">
  <h1>사고싶은 책 목록</h1>
  <ul class="items">
    <li>리액트를 다루는 기술</li>
    <li>Do it! 안드로이드 앱 프로그래밍</li>
    <li>프로그래밍 면접, 이렇게 준비한다</li>
  </ul>
</div>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')
#필요한 부분을 CSS 쿼리로 추출하기
#soup.select_one(<선택자>) => 요소하나 추출
#선택자 div#meigen의 의미 => div#meigen(id명) Header에 소속된 h1의 내용
h1 = soup.select_one("div#meigen > h1").string
print("h1 =", h1)
#soup.select(<선택자>) => 요소 여러 개를 리스트로 추출
#ul.items(class명)
li_list = soup.select("div#meigen > ul.items > li")
for li in li_list:
  print("li =", li.string)