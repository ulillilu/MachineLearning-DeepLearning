import tensorflow as tf

tf.compat.v1.disable_eager_execution()
a = tf.compat.v1.placeholder(tf.int32) # 정수 자료형 배열 선언
# 배열을 모든 값을 2배하는 연산 정의
b = tf.constant(2)
x2_op = a * b

sess = tf.compat.v1.Session()

r1 = sess.run(x2_op, feed_dict={ a:[1, 2, 3] })
print(r1)
r2 = sess.run(x2_op, feed_dict={ a:[10, 20, 10] })
print(r2)