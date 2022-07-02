import tensorflow as tf
tf.random.set_random_seed(seed=2)

a = tf.Variable(tf.random_normal([2, 2]) * tf.sqrt(0.5))
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(a))