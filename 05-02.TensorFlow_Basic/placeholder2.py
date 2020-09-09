import tensorflow as tf

tf.compat.v1.disable_eager_execution()
a = tf.compat.v1.placeholder(tf.int32, shape=[None])
b = tf.constant(10)
x10_op = a * b

sess = tf.compat.v1.Session()

r1 = sess.run(x10_op, feed_dict={a: [1,2,3,4,5]})
print(r1)
r2 = sess.run(x10_op, feed_dict={a: [10,20]})
print(r2)