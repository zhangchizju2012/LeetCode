#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 22:32:40 2018

@author: zhangchi
"""

#import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

nparray = np.array([[1.,2.],[2.,3.]])
tfarray = tf.convert_to_tensor(nparray)

with tf.Session() as sess:
    print(sess.run(tf.exp(tfarray)))