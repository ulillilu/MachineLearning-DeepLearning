# 학습한 매개변수를 저장하는 프로그램
from sklearn import svm 
from sklearn.externals import joblib
import json
# 각 언어의 출현 빈도 데이터(JSON) 읽기
with open("./lang/freq.json", "r", encoding="utf-8") as fp:
    d = json.load(fp)
    data = d[0]
# 데이터 학습
clf = svm.SVC()
clf.fit(data["freqs"], data["labels"])
# 학습 데이터 저장
joblib.dump(clf, "./lang/freq.pkl")
print("ok")