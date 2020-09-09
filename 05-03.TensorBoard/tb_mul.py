import tensorflow as tf
tf.compat.v1.disable_eager_execution()

a = tf.constant(20, name="a")
b = tf.constant(30, name="b")
mul_op = a * b

sess = tf.compat.v1.Session()
# TensorBoard 그리기
tw = tf.compat.v1.summary.FileWriter("log_dir", graph=sess.graph)
result = sess.run(mul_op)
print(result)
