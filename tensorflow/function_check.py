#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:32:40 2018

@author: zhangchi
"""

#import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

# test for knn.py

compare_nparray = np.array([[1.,2.,3.],[2.,3.,4.],[2.,2.,4.],[2.,2.,3.]])
input_nparray = np.array([2.,2.,2.])
label_nparray = np.array([2,0,2,8])


compare_tfarray = tf.convert_to_tensor(compare_nparray)
input_tfarray = tf.convert_to_tensor(input_nparray)
label_tfarray = tf.convert_to_tensor(label_nparray)

with tf.Session() as sess:
    print(sess.run(compare_tfarray - input_tfarray))
    #print(sess.run(tf.square(compare_tfarray - input_tfarray)))
    #print(sess.run(tf.squared_difference(compare_tfarray, input_tfarray)))
    #print(sess.run(tf.reduce_sum(tf.squared_difference(compare_tfarray, input_tfarray),axis=1)))
    distance = -1 * tf.reduce_sum(tf.squared_difference(compare_tfarray, input_tfarray),axis=1)
    indices = tf.nn.top_k(distance,3).indices
    labels = tf.gather(label_tfarray, indices)
    count = tf.unique_with_counts(labels)
    max_count_index = tf.argmax(count.count)
    predict = count.y[max_count_index]
    print(sess.run(distance))
    print(sess.run(indices[0]))
    print(sess.run(labels))
    #print(sess.run(count))
    print(sess.run(max_count_index))
    print(sess.run(predict))
# =============================================================================
# nparray = np.array([[1.,2.,3.],[2.,3.,4.]])
# tfarray = tf.convert_to_tensor(nparray)
# test for exponential.py
# 
# with tf.Session() as sess:
#     print(sess.run(tf.exp(tfarray)))
#     print(sess.run(tf.nn.top_k(tfarray,2).indices))
# =============================================================================
