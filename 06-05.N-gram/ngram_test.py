# N-gram으로 유사도 구하기
def ngram(s, num): # (입력문자열/글자 분할 단위)
    res = []
    slen = len(s) - num + 1 # 분할 단어 수
    for i in range(slen):
        ss = s[i:i+num] # 분할된 단어
        res.append(ss)
    return res

def diff_ngram(sa, sb, num):
    a = ngram(sa, num)
    b = ngram(sb, num)
    r = []
    cnt = 0
    for i in a:
        for j in b:
            if i == j:
                cnt += 1 # 비교 단어가 같으면 cnt 증가
                r.append(i)
    return cnt / len(a), r # 단어가 일치하는 비율과 분할된 문장 출력
a = "오늘 강남에서 맛있는 스파게티를 먹었다."
b = "강남에서 먹었던 오늘의 스파게티는 맛있었다."
# 2-gram
r2, word2 = diff_ngram(a, b, 2)
print("2-gram:", r2, word2)
# 3-gram
r3, word3  = diff_ngram(a, b, 3)
print("3-gram:", r3, word3)