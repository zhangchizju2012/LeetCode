import tensorflow as tf
import numpy as np

he_normal = tf.keras.initializers.he_normal()

def batch_norm_layer(inputs, is_training, momentum=0.9, epsilon=1e-5, in_place_update=True, name="batch_norm"):
    '''
    Helper function to create a batch normalization layer
    '''
    if in_place_update:
        return tf.contrib.layers.batch_norm(inputs, decay=momentum, epsilon=epsilon,
                                            center=True, scale=True, updates_collections=None,
                                            is_training=is_training, scope=name)
    else:
        return tf.contrib.layers.batch_norm(inputs, decay=momentum, epsilon=epsilon,
                                            center=True, scale=True, is_training=is_training, scope=name)


def conv_layer(inputs, name, filter_height, filter_width, in_channels, out_channels):
    with tf.variable_scope("conv_block_%s" % name):
        # Convolution Layer
        # [filter_height, filter_width, in_channels, out_channels]
        # out_channels = 32
        filter_shape = [filter_height, filter_width, in_channels, out_channels]#[5, 5, 3, out_channels]
        W = tf.get_variable(name='W', shape=filter_shape, initializer=he_normal)
        b = tf.get_variable(name='b', shape=[out_channels], initializer=tf.constant_initializer(0.0))
        #W = tf.Variable(tf.truncated_normal(filter_shape, stddev=0.1), name="W",initializer=he_normal)
        #b = tf.Variable(tf.constant(0.1, shape=[out_channels]), name="b")
        # stride is the size of each step
        conv = tf.nn.conv2d(
          inputs,
          W,
          strides=[1, 1, 1, 1],
          padding="SAME",
          name="conv") + b
    return conv

# =============================================================================
# def conv_batch_relu(inputs, name, is_training, filter_height, filter_width, in_channels, out_channels):
#     conv = conv_layer(inputs, name, filter_height, filter_width, in_channels, out_channels)
#     batch = batch_norm_layer(conv, is_training, name = "batch-"+str(name))
#     return tf.nn.relu(batch)
# =============================================================================

def conv_batch_relu(inputs, is_training, filter_height, filter_width, in_channels, out_channels):
    x = conv_layer(inputs, 1, filter_height, filter_width, in_channels, out_channels)
    x = batch_norm_layer(x, is_training, name = "batch-1")
    return tf.nn.relu(x)

def batch_relu_conv(inputs, is_training, filter_height, filter_width, in_channels, out_channels):
    x = batch_norm_layer(inputs, is_training, name = "batch-1")
    x = tf.nn.relu(x)
    return conv_layer(x, 1, filter_height, filter_width, in_channels, out_channels)

def batch_relu(inputs, is_training):
    x = batch_norm_layer(inputs, is_training, name = "batch-1")
    return tf.nn.relu(x)

def residual(inputs, is_training, filter_height, filter_width, in_channels, mid_channels, out_channels):
    origin_inputs = inputs
    
    x = batch_norm_layer(inputs, is_training, name = "batch-1")
    x = tf.nn.relu(x)
    x = conv_layer(x, 1, filter_height, filter_width, in_channels, mid_channels)
    
    x = batch_norm_layer(x, is_training, name = "batch-2")
    x = tf.nn.relu(x)
    x = conv_layer(x, 2, filter_height, filter_width, mid_channels, out_channels)
    
    return origin_inputs + x
    
    

# =============================================================================
# def Conv(inputs, num_filters, is_training, name):
#     # Conv2D + Batch norm + ReLU layers
#     with tf.variable_scope("conv_block_%s" % name):
#         filter_shape = [3, 3, inputs.get_shape()[3], num_filters]
#         w = tf.get_variable(name='W_1', shape=filter_shape, 
#             initializer=he_normal)
#         b = tf.get_variable(name='b_1', shape=[num_filters], 
#                 initializer=tf.constant_initializer(0.0))
#         conv = tf.nn.conv2d(inputs, w, strides=[1, 1, 1, 1], padding="SAME") + b
#     return conv
# =============================================================================


