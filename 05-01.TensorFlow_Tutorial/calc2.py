import tensorflow as tf

a = tf.constant(2, dtype=tf.int32)
b = tf.constant(3, dtype=tf.int32)
c = tf.constant(4, dtype=tf.int32)

calc1_op = a + b * c
calc2_op = (a + b) * c

tf.print(calc1_op)
tf.print(calc2_op)