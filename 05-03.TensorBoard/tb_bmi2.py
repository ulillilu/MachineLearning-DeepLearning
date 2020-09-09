import pandas as pd
import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

csv = pd.read_csv("bmi.csv")

csv["height"] = csv["height"] / 200
csv["weight"] = csv["weight"] / 100

bclass = {"thin": [1,0,0], "normal": [0,1,0], "fat": [0,0,1]}
csv["label_pat"] = csv["label"].apply(lambda x : np.array(bclass[x]))

test_csv = csv[15000:20000]
test_pat = test_csv[["weight","height"]]
test_ans = list(test_csv["label_pat"])

x  = tf.compat.v1.placeholder(tf.float32, [None, 2], name="x") 
y = tf.compat.v1.placeholder(tf.float32, [None, 3], name="y_") 

# interface 부분을 스코프로 묶기
with tf.name_scope('interface') as scope:
    W = tf.Variable(tf.zeros([2, 3]), name="W");
    b = tf.Variable(tf.zeros([3]), name="b");

    with tf.name_scope('softmax') as scope:
        z = tf.nn.softmax(tf.matmul(x, W) + b)

#  loss 계산을 스코프로 묶기
with tf.name_scope('loss') as scope:
    cross_entropy = -tf.reduce_sum(y * tf.compat.v1.log(z))

# training 계산을 스코프로 묶기
with tf.name_scope('training') as scope:
    optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.01)
    train = optimizer.minimize(cross_entropy)

#  accuracy 계산을 스코프로 묶기
with tf.name_scope('accuracy') as scope:
    predict = tf.equal(tf.argmax(z, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(predict, tf.float32))

with tf.compat.v1.Session() as sess:
    # TensorBoard를 사용하는 부분
    tw = tf.compat.v1.summary.FileWriter("log_dir", graph=sess.graph)
    sess.run(tf.compat.v1.global_variables_initializer()) # 변수 초기화
    
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

    acc = sess.run(accuracy, feed_dict={x: test_pat, y: test_ans})
    print("정답률=", acc)
            
