# 생성한 데이터를 통한 머신러닝 학습
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
# 데이터 읽기
tbl = pd.read_csv("bmi.csv")
# 칼럼(열)을 자르고 정규화
label = tbl["label"] #label열의 정보를 label에 저장
w = tbl["weight"] / 100
h = tbl["height"] / 200
wh = pd.concat([w, h], axis=1) #pandas를 이용하여 배열 전체 요소에 연산 적용

data_train, data_test, label_train, label_test = \
    train_test_split(wh, label)

clf = svm.SVC()
clf.fit(data_train, label_train)
predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)