# 메서드를 사용한 교차 검증
import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

csv = pd.read_csv('iris.csv')

data = csv[["SepalLength","SepalWidth","PetalLength","PetalWidth"]]
label = csv["Name"]
# 교차 검증 하기
clf = svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5) #cv=교차 검증 하고 싶은 횟수
print("각각의 정답률 =", scores)
print("평균 정답률 =", scores.mean())