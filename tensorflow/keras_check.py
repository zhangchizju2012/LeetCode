#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 23:09:36 2018

@author: zhangchi
"""

import keras.backend as K
import numpy as np
from keras.layers.core import *
from keras.layers import merge

A = np.array([[1,2,3],[4,5,6]])
#B = np.random.rand(500,6000)

x = K.variable(value=A)
#y = K.variable(value=B)

#z = K.dot(x,y)

# Here you need to use K.eval() instead of z.eval() because this uses the backend session
print(K.eval(merge([x,x],mode='mul')))