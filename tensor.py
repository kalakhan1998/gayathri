import tensorflow as tf
hello = tf.constant("hello tensor")
sess = tf.session()
print(sess.run(hello))
