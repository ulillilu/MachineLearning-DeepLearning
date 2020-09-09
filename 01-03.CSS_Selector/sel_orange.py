#여러 방법으로 추출하기
from bs4 import BeautifulSoup 
fp = open("fruits-vegetables.html", encoding="utf-8")
soup = BeautifulSoup(fp, "html.parser")
# CSS 선택자로 추출하기
print(soup.select_one("li:nth-of-type(4)").string)
print(soup.select_one("#fr-list > li:nth-of-type(4)").string)
print(soup.select("#fr-list > li[data-lo='ko']")[1].string)
print(soup.select("#fr-list > li.yellow")[1].string)
# find 메서드로 추출하기 
cond = {"data-lo":"ko", "class":"yellow"}
print(soup.find("li", cond).string)
# find 메서드를 연속적으로 사용하기
print(soup.find(id="fr-list")
           .find("li", cond).string)