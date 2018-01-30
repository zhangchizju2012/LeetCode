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
    batch_size = 5
    
    # parameters settings
    mnist = read_data_sets("data", one_hot=True)
    x_train, y_train = mnist.train.images, mnist.train.labels
    shape = y_train.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if y_train[i,j] == 0.:
                y_train[i,j] = -1.
    
    # Define placeholders for input
    X = tf.placeholder(tf.float32, shape=(batch_size, 784))
    y = tf.placeholder(tf.float32, shape=(batch_size, 10))
    
    with tf.variable_scope("support-vector-machine"):
        W = tf.get_variable("weights", (784, 10),
                            initializer=tf.random_normal_initializer())
        b = tf.get_variable("bias", (10,),
                            initializer=tf.random_normal_initializer())
                            #initializer=tf.constant_initializer(0.0))
        y_pred = tf.matmul(X, W) + b
        temp = tf.maximum(0., 1 - tf.multiply(y, y_pred))
        loss = tf.reduce_sum(temp, axis = 0)
        
    with tf.Session() as sess:
        # Initialize Variables in graph
        sess.run(tf.global_variables_initializer())
        indices = np.random.choice(n_samples, batch_size)
        X_batch, y_batch = x_train[indices], y_train[indices]
        #y_batch = np.reshape(y_batch, (batch_size,1))
        temp_, loss_ = sess.run([temp, loss], feed_dict={X: X_batch, y: y_batch})
        print(temp_)
        print(loss_)
    
    predicted_y_test = []
    
    return predicted_y_test



def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    run()
    # hyperparameters_search()

