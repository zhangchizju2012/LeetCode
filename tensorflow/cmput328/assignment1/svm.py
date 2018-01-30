#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:07:21 2018

@author: zhangchi
"""

import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import timeit


def run():#x_test):
    n_samples = 55000
    batch_size = 10
    
    # parameters settings
    mnist = read_data_sets("data", one_hot=False)
    x_train, y_train = mnist.train.images, mnist.train.labels
    
    # Define placeholders for input
    X = tf.placeholder(tf.float32, shape=(batch_size, 784))
    y = tf.placeholder(tf.float32, shape=(batch_size, 1))
    
    with tf.variable_scope("support-vector-machine"):
        W = tf.get_variable("weights", (784, 1),
                            initializer=tf.random_normal_initializer())
        b = tf.get_variable("bias", (1,),
                            initializer=tf.constant_initializer(0.0))
        y_pred = tf.matmul(X, W) + b
        temp = tf.maximum(0., 1 - tf.multiply(y, y_pred))
        #loss = tf.reduce_sum((y - y_pred)**2)
        
    with tf.Session() as sess:
        # Initialize Variables in graph
        sess.run(tf.initialize_all_variables())
        indices = np.random.choice(n_samples, batch_size)
        X_batch, y_batch = x_train[indices], y_train[indices]
        y_batch = np.reshape(y_batch, (batch_size,1))
        y_pred_, y_, temp_ = sess.run([y_pred, y, temp], feed_dict={X: X_batch, y: y_batch})
        print(y_batch)
        print(y_pred_)
        print(y_)
        print(temp_)
        #_, loss_val, W_, b_ = sess.run([opt_operation, loss, W, b], feed_dict={X: X_batch, y: y_batch})
        #print loss_val
        #print(str(loss_val)+ " "+ str(W_)+" "+str(b_))
    
    predicted_y_test = []
    
    return predicted_y_test



def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    run()
    # hyperparameters_search()

