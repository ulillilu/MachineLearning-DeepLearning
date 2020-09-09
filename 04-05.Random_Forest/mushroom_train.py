import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split

mr = pd.read_csv("mushroom.csv", header=None)
# 데이터 내부의 기호(알파벳)를 숫자로 변환
label = []
data = []
attr_list = []
for row_index, row in mr.iterrows():
    label.append(row.iloc[0]) #iloc:순서를 나타내는 정수 기반의 2차원 인덱싱
    row_data = []
    for v in row.iloc[1:]: #Header(1번째 줄)을 제외한 모든 줄에 대하여 반복
        row_data.append(ord(v)) #ord() 문자의 아스키 코드 값을 반환
    data.append(row_data)

data_train, data_test, label_train, label_test = \
    train_test_split(data, label)
#RandomForest를 통해 학습
clf = RandomForestClassifier()
clf.fit(data_train, label_train)

predict = clf.predict(data_test)

ac_score = metrics.accuracy_score(label_test, predict)
cl_report = metrics.classification_report(label_test, predict)
print("정답률 =", ac_score)
print("리포트 =\n", cl_report)