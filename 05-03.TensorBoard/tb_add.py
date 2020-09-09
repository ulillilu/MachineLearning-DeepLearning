import tensorflow as tf
tf.compat.v1.disable_eager_execution()

a = tf.constant(100, name="a")
b = tf.constant(200, name="b")
c = tf.constant(300, name="c")
v = tf.Variable(0, name="v")

calc_op = a + b * c 
assign_op = tf.compat.v1.assign(v, calc_op) # 변수에 대입하는 그래프 정의

sess = tf.compat.v1.Session()
# TensorBoard
tw = tf.compat.v1.summary.FileWriter("log_dir", graph=sess.graph)

sess.run(assign_op)
print(sess.run(v))