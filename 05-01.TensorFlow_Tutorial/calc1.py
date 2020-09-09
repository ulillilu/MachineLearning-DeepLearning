import tensorflow as tf
# 상수 정의
a = tf.constant(1234, dtype=tf.int32)
b = tf.constant(5000)
# 계산 정의
add_op = a + b
# 세션 시작
tf.print(add_op)