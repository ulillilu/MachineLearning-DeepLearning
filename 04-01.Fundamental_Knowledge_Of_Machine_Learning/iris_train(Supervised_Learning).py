# 데이터를 기반으로 붓꽃 품종 분류
from sklearn import svm, metrics
import random, re
# csv data 읽기
csv = []
with open('iris.csv', 'r', encoding='utf-8') as fp:
    # 한 줄씩 읽기
    for line in fp:
        line = line.strip()    # 줄바꿈 제거
        cols = line.split(',') # 쉼표로 자르기
        # 문자열 데이터를 숫자로 변환
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n #Python의 삼항 연산자 lambda n:(값)=(True일 때의 값) if (조건) else (False일 때의 값)
        cols = list(map(fn, cols))
        csv.append(cols)
# Header 제거
del csv[0]
# 데이터 셔플
random.shuffle(csv)
# 학습 전용 데이터와 테스트 전용 데이터 분할(2:1 비율)
total_len = len(csv) #150개
train_len = int(total_len * 2 / 3) #100개
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data  = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)

clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

ac_score = metrics.accuracy_score(test_label, pre)
print("정답률 =", ac_score)