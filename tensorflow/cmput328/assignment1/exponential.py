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
    n_samples = 55000
    # made change
    batch_size = 256 # 5
    lr = 1e-5
    C = 1
    num_epochs = 50
    
    # parameters settings
    mnist = read_data_sets("data", one_hot=True)
    x_train, y_train = mnist.train.images, mnist.train.labels
    shape = y_train.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            if y_train[i,j] == 0.:
                y_train[i,j] = -1.
    
    # Define placeholders for input
    # Pay attention to None here, I use batch_size originally
    # None can handle any size, which is better.
    X = tf.placeholder(tf.float32, shape=(None, 784))
    y = tf.placeholder(tf.float32, shape=(None, 10))
    
    with tf.variable_scope("exponential"):
        # made change
        W = tf.Variable(tf.random_normal(shape=[28*28, 10],stddev=0.1),dtype=tf.float32)
        #W = tf.get_variable("weights", (784, 10),
        #                    initializer=tf.random_normal_initializer())
        b = tf.get_variable("bias", (10,),
                            #initializer=tf.random_normal_initializer())
                            initializer=tf.constant_initializer(0.0))
        y_pred = tf.matmul(X, W) + b
        pred_result = tf.argmax(y_pred, 1)
        correct_predictions = tf.equal(tf.argmax(y, 1), pred_result)
        accuracy = tf.reduce_mean(tf.cast(correct_predictions, "float"))
        left = tf.multiply(W, W)
        # made change
        right = tf.exp(-1. * tf.multiply(y, y_pred))
        # all these three are ok.
        loss = tf.reduce_mean(left, axis = 0) * 0.5 + C * tf.reduce_sum(right, axis = 0)
        #loss = tf.reduce_mean(left) * 0.5 + C * tf.reduce_sum(right)
        #loss =C*tf.losses.hinge_loss(logits=y_pred, labels=y)*500. + 0.5*tf.reduce_mean(tf.square(W))


    operation = tf.train.GradientDescentOptimizer(learning_rate=lr).minimize(loss)
    
    with tf.Session() as sess:
        # Initialize Variables in graph
        sess.run(tf.global_variables_initializer())
        
        predicted_y_test = []
        
        for epoch in range(num_epochs):
            num_batches = n_samples // batch_size
            for iteration in range(num_batches):
                indices = np.random.choice(n_samples, batch_size)
                X_batch, y_batch = x_train[indices], y_train[indices]
                #x_train_batch, y_train_batch = mnist.train.next_batch(batch_size)
                _, loss_, acc = sess.run([operation, loss, accuracy], feed_dict={X: X_batch, y: y_batch})
            print("epoch:",epoch, "loss:", loss_, "acc:",acc)
            
        num_test_batches = len(x_test) // batch_size
        for iteration in range(num_test_batches + 1):
            if iteration != num_test_batches:
                x_test_batch = x_test[:batch_size]
                x_test = x_test[batch_size:]
            else:
                x_test_batch = x_test[:len(x_test)]
                x_test = x_test[len(x_test):]
            result = sess.run([pred_result], feed_dict={X: x_test_batch})[0]
            # pay attention to [0] and tolist() here
            predicted_y_test += result.tolist()
            
        print(predicted_y_test)
    
    return predicted_y_test



def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    run()
    # hyperparameters_search()

