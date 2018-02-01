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


def run(x_test):
    k = 1
    
    # parameters settings
    
    mnist = read_data_sets("data", one_hot = False)
    x_train, y_train = mnist.train.images, mnist.train.labels
    
    # Define placeholders for input
    # Pay attention to None here, I use batch_size originally
    # None can handle any size, which is better.
    X = tf.placeholder(tf.float32, shape=(784,))
    
    with tf.variable_scope("knn"):
        distance = -1 * tf.reduce_sum(tf.squared_difference(x_train, X),axis=1)
        indices = tf.nn.top_k(distance,k).indices
        labels = tf.gather(y_train, indices)
        count = tf.unique_with_counts(labels)
        max_count_index = tf.argmax(count.count)
        predict = count.y[max_count_index]
    
    with tf.Session() as sess:
        # Initialize Variables in graph
        # sess.run(tf.global_variables_initializer())
        
        predicted_y_test = []
        
        for index, item in enumerate(x_test):
            pred = sess.run([predict], feed_dict={X: item})[0]
            predicted_y_test.append(pred)
            print(index)
            
        print(predicted_y_test)
    
    return predicted_y_test



def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    run()
    # hyperparameters_search()

