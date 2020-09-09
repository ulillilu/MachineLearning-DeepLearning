import tensorflow as tf

a = tf.constant(120, name="a")
b = tf.constant(130, name="b")
c = tf.constant(140, name="c")
# 변수 정의
v = tf.Variable(0, name="v")
# 연산 후 결과를 변수에 대입
calc_op = a + b + c
assign_op = tf.compat.v1.assign(v, calc_op) #tf.assign => tf.compat.v1.assign

tf.print(v)