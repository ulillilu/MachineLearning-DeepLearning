# 언어 판별 프로그램
from sklearn import svm, metrics
import glob, os.path, re, json
# 텍스트를 읽어 들이고 출현 빈도 조사
def check_freq(fname):
    name = os.path.basename(fname)
    # 파일명 맨 앞의 두글자 추출
    lang = re.match(r'^[a-z]{2,}', name).group()
    # 파일 내용 읽기
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    text = text.lower() # 소문자 변환
    # 숫자 세기 변수(cnt) 초기화하기
    cnt = [0 for n in range(0, 26)]
    code_a = ord("a")
    code_z = ord("z")
    # 알파벳 출현 횟수 구하기
    for ch in text:
        n = ord(ch)
        if code_a <= n <= code_z: # a~z 사이에 있을 때
            cnt[n - code_a] += 1
    # 정규화
    total = sum(cnt)
    freq = list(map(lambda n: n / total, cnt)) # 출현 횟수/글자 수 합계 = 알파벳 출현 빈도
    return (freq, lang)
    
# 각 파일 처리
def load_files(path):
    freqs = []
    labels = []
    file_list = glob.glob(path)
    for fname in file_list:
        r = check_freq(fname)
        freqs.append(r[0])
        labels.append(r[1])
    return {"freqs":freqs, "labels":labels}
    
data = load_files("./lang/train/*.txt")
test = load_files("./lang/test/*.txt")
# JSON으로 결과 저장
with open("./lang/freq.json", "w", encoding="utf-8") as fp:
    json.dump([data, test], fp)

clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])
predict = clf.predict(test["freqs"])
# 결과 테스트
ac_score = metrics.accuracy_score(test["labels"], predict)
cl_report = metrics.classification_report(test["labels"], predict)
print("정답률 =", ac_score)
print("리포트 =")
print(cl_report)