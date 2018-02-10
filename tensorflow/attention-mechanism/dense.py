#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 21:11:43 2018

@author: zhangchi
"""

# reimplement attention_dense.py using pure TensorFlow.

import numpy as np
import tensorflow as tf

input_dim = 32

he_normal = tf.keras.initializers.he_normal()

def get_data(n, input_dim, attention_column=1):
    """
    Data generation. x is purely random except that it's first value equals the target y.
    In practice, the network should learn that the target = x[attention_column].
    Therefore, most of its attention should be focused on the value addressed by attention_column.
    :param n: the number of samples to retrieve.
    :param input_dim: the number of dimensions of each element in the series.
    :param attention_column: the column linked to the target. Everything else is purely random.
    :return: x: model inputs, y: model targets
    """
    x = np.random.standard_normal(size=(n, input_dim))
    y = np.random.randint(low=0, high=2, size=(n, 1))
    x[:, attention_column] = y[:, 0]
    return x, y

def Net(inputs):
    
    with tf.variable_scope("attention"):
        W_0 = tf.get_variable('W', [input_dim, input_dim], initializer=he_normal)
        b_0 = tf.get_variable('b', [input_dim], initializer=tf.constant_initializer(0.0))
        before_activation = tf.matmul(inputs, W_0) + b_0
        attention_probs = tf.nn.softmax(before_activation)
        attention_mul = tf.multiply(inputs, attention_probs)
    
    with tf.variable_scope("fully-connected-1"):
        W_1 = tf.get_variable('W', [input_dim, 64], initializer=he_normal)
        b_1 = tf.get_variable('b', [64], initializer=tf.constant_initializer(0.0))
        attention_mul = tf.matmul(attention_mul, W_1) + b_1
        
    with tf.variable_scope("fully-connected-2"):
        W_2 = tf.get_variable('W', [64, 1], initializer=he_normal)
        b_2 = tf.get_variable('b', [1], initializer=tf.constant_initializer(0.0))
        before_activation = tf.matmul(attention_mul, W_2) + b_2
        output = tf.nn.sigmoid(before_activation)
        
    return output

def train():
    # input Tensors
    X = tf.placeholder(tf.float32, shape=[None, input_dim], name='x')
    y = tf.placeholder(tf.float32, shape=[None, 1], name='y')
    output = Net(X)
    loss = tf.keras.backend.binary_crossentropy(y, output)
    operation = tf.train.AdamOptimizer().minimize(loss)
    