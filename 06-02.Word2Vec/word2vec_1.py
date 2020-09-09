import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from gensim.models import word2vec

fp = codecs.open("4BH00002.txt", "r", encoding="utf-16")
soup = BeautifulSoup(fp, "html.parser")
body = soup.select_one("text > body")
text = body.getText()

okt = Okt()
results = []
lines = text.split("\r\n")
for line in lines:
    # 단어의 기본형을 사용하여 형태소 분석
    malist = okt.pos(line, norm=True, stem=True)
    r = []
    for word in malist:
        # 어미/조사/구두점 등은 분석 대상에서 제외 
        if not word[1] in ["Josa", "Eomi", "Punctuation"]:
            r.append(word[0])
    rl = (" ".join(r)).strip() # 형태소 마다 띄어쓰기
    results.append(rl) # 기본형 형태소를 리스트에 저장
    print(rl)

gubun_file = 'text.gubun'
with open(gubun_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))
# Word2Vec 모델 만들기
data = word2vec.LineSentence(gubun_file)
model = word2vec.Word2Vec(data, 
    size=200, window=10, hs=1, min_count=2, sg=1)
model.save("text.model")
print("ok")