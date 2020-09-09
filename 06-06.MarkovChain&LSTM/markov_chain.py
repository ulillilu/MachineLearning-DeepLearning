import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Okt
import urllib.request
import os, re, json, random

def make_dic(words):
    tmp = ["@"] # 문장 시작 기호
    dic = {}
    for word in words:
        tmp.append(word) # tmp에 한 문장에 속한 단어 등록
        if len(tmp) < 3: continue
        if len(tmp) > 3: tmp = tmp[1:] 
        set_word3(dic, tmp) # tmp의 단어를 3개 단위로 dictionary에 등록(해당 세 단어는 서로 인접)
        if word == ".": # 문장이 끝난 경우
            tmp = ["@"] # tmp를 다시 초기화
            continue
    return dic
# 한 문장에 속한 단어를 세 개 단위로 dictionary에 등록
def set_word3(dic, s3):
    w1, w2, w3 = s3
    if not w1 in dic: dic[w1] = {} # dictionary에 단어 항목이 없는 경우 생성 ex){'apple':{}} 
    if not w2 in dic[w1]: dic[w1][w2] = {}  # dictionary에 단어 항목이 없는 경우 생성 ex){'apple':{'blue':{}}} 
    if not w3 in dic[w1][w2]: dic[w1][w2][w3] = 0 # dictionary에 단어 항목이 없는 경우 생성 ex){'apple':{'blue':{'berry':{0}}}} 
    dic[w1][w2][w3] += 1
# 문장 만들기
def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic" 
    top = dic["@"]
    w1 = word_choice(top) # 무작위 단어 선택
    w2 = word_choice(top[w1]) # 선택된 단어와 인접한 단어 선택
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2]) # w1 w2와 인접한 단어 중 하나 무작위 선택
        ret.append(w3)
        if w3 == ".": break # w3가 .을 포함한 단어인 경우 반복 중지
        w1, w2 = w2, w3
    ret = "".join(ret)
    # # 띄어쓰기
    # params = urllib.parse.urlencode({
    #     "_callback": "",
    #     "q": ret
    # })
    # # 네이버 맞춤법 검사기 사용
    # site = "https://m.search.naver.com/p/csearch/ocontent/util/SpellerProxy" + "?" + params
    # hdr = {'User-Agent': 'Mozilla/5.0', 'referer':'https://www.naver.com/'}
    # reqUrl = urllib.request.Request(site, hdr)
    # data = urllib.request.urlopen(reqUrl)
    # data = data.read().decode("utf-8")[1:-2]
    # data = json.loads(data)
    # data = data["message"]["result"]["html"]
    # data = soup = BeautifulSoup(data, "html.parser").getText()
    return ret

def word_choice(sel): # 키를 이용하여 dictionary의 단어 무작위 선택
    keys = sel.keys()
    return random.choice(list(keys))
# 문장 읽기
dict_file = "markov-text.json"
if not os.path.exists(dict_file):
    fp = codecs.open("4BH00002.txt", "r", encoding="utf-16")
    soup = BeautifulSoup(fp, "html.parser")
    body = soup.select_one("text > body")
    text = body.getText()
    text = text.replace("…", "") # 현재 koNLPy가 …을 구두점으로 잡지 못하는 문제 임시 해결
    # 형태소 분석
    okt = Okt()
    malist = okt.pos(text, norm=True)
    words = []
    for word in malist:
        if not word[1] in ["Punctuation"]:
            words.append(word[0])
        if word[0] == ".":
            words.append(word[0])

    dic = make_dic(words)
    json.dump(dic, open(dict_file,"w", encoding="utf-8"))
else:
    dic = json.load(open(dict_file,"r"))
# 문장 만들기
for i in range(3):
    s = make_sentence(dic)
    print(s)
    print("---")