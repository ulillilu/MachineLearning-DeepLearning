import pandas as pd
import numpy as np
import tensorflow as tf

csv = pd.read_csv("bmi.csv")
# 정규화
csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100
# 레이블을 배열로 변환
bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))
# 테스트를 위한 데이터 분류
test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

tf.compat.v1.disable_eager_execution()
x  = tf.compat.v1.placeholder(tf.float32, shape=[None, 2]) # 키와 몸무게 데이터
y = tf.compat.v1.placeholder(tf.float32, shape=[None, 3]) # 정답 레이블

W = tf.Variable(tf.zeros([2, 3])); # 가중치 영행렬
b = tf.Variable(tf.zeros([3])); # 편차치 영행렬
# 소프트맥스 회귀 정의
z = tf.nn.softmax(tf.matmul(x, W) + b)
# 모델 훈련
cross_entropy = -tf.reduce_sum(y * tf.compat.v1.log(z))
# 오차 함수가 최소가 되게 학습(가중치와 편차치의 값 자동 변경)
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.01) # 0.01 = 학습 계수/경사 하강법
train = optimizer.minimize(cross_entropy)
# 정답률 구하기
predict = tf.equal(tf.argmax(z, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

sess = tf.compat.v1.Session()
sess.run(tf.compat.v1.global_variables_initializer()) # 변수 초기화하기
# 학습시키기
for step in range(3500):
    i = (step * 100) % 14000
    rows = csv[1 + i : 1 + i + 100]
    x_pat = rows[["weight","height"]]
    y_ans = list(rows["label_pat"])
    fd = {x: x_pat, y: y_ans}
    sess.run(train, feed_dict=fd)
    if step % 500 == 0:
        cre = sess.run(cross_entropy, feed_dict=fd)
        acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
        print("step=", step, "cre=", cre, "acc=", acc)
# 최종적인 정답률
acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
print("정답률 =", acc)