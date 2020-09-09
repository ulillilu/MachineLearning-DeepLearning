from sklearn import svm, metrics
import random, re

lines = open('iris.csv', 'r', encoding='utf-8').read().split("\n")
f_tonum = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
f_cols  = lambda li: list(map(f_tonum,li.strip().split(',')))
csv = list(map(f_cols, lines))
del csv[0] # 헤더 제거
random.shuffle(csv)
# 데이터를 K개로 분할(K개의 데이터 그룹으로 나눔)
K = 5 
csvk = [ [] for i in range(K) ]
for i in range(len(csv)):
    csvk[i % K].append(csv[i])
# 리스트를 훈련 전용 데이터와 테스트 전용 데이터로 분할
def split_data_label(rows):
    data = []; label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])
    return (data, label)
# 정답률 구하기
def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)
    # 학습시키고 정답률 구하기
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)
# 교차 검증
score_list = []
for testc in csvk:
    # testc 이외의 데이터를 훈련 전용 데이터로 사용/K개의 그룹이 번갈아가면서 테스트 데이터와와 훈련 데이터로 사용됨
    trainc = []
    for i in csvk:
        if i != testc: trainc += i
    sc = calc_score(testc, trainc) # 각 경우별 정답률 구함
    score_list.append(sc)
print("각각의 정답률 =", score_list)
print("평균 정답률 =", sum(score_list) / len(score_list))