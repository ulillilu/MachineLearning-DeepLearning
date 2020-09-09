import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt

fp = codecs.open("4BH00002.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

okt = Okt()
word_dic = {}
lines = text.split("\n") # 텍스트 한 줄씩 나누기

for line in lines:
    malist = okt.pos(line) # 형태소 추출
    for word in malist:
        if word[1] == "Noun": #  명사 확인
            if not (word[0] in word_dic):
                word_dic[word[0]] = 0
            word_dic[word[0]] += 1

keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print()