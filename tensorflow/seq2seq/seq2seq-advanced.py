
import numpy as np
import tensorflow as tf
import helpers

tf.reset_default_graph()
sess = tf.InteractiveSession()

PAD = 0
EOS = 1

vocab_size = 10
input_embedding_size = 20

encoder_hidden_units = 20
decoder_hidden_units = encoder_hidden_units * 2

encoder_inputs = tf.placeholder(shape=(None, None), dtype=tf.int32, name='encoder_inputs')
encoder_inputs_length = tf.placeholder(shape=(None,), dtype=tf.int32, name='encoder_inputs_length')

decoder_targets = tf.placeholder(shape=(None, None), dtype=tf.int32, name='decoder_targets')

embeddings = tf.Variable(tf.random_uniform([vocab_size, input_embedding_size], -1.0, 1.0), dtype=tf.float32)

encoder_inputs_embedded = tf.nn.embedding_lookup(embeddings, encoder_inputs)

from tensorflow.contrib.rnn import LSTMCell, LSTMStateTuple

encoder_cell = LSTMCell(encoder_hidden_units)

((encoder_fw_outputs,
  encoder_bw_outputs),
 (encoder_fw_final_state,
  encoder_bw_final_state)) = (
    tf.nn.bidirectional_dynamic_rnn(cell_fw=encoder_cell,
                                    cell_bw=encoder_cell,
                                    inputs=encoder_inputs_embedded,
                                    sequence_length=encoder_inputs_length,
                                    dtype=tf.float32, time_major=True)
    )


encoder_outputs = tf.concat((encoder_fw_outputs, encoder_bw_outputs), 2)

encoder_final_state_c = tf.concat(
    (encoder_fw_final_state.c, encoder_bw_final_state.c), 1)

encoder_final_state_h = tf.concat(
    (encoder_fw_final_state.h, encoder_bw_final_state.h), 1)

encoder_final_state = LSTMStateTuple(
    c=encoder_final_state_c,
    h=encoder_final_state_h
)


decoder_cell = LSTMCell(decoder_hidden_units)

encoder_max_time, batch_size = tf.unstack(tf.shape(encoder_inputs))

decoder_lengths = encoder_inputs_length + 3

W = tf.Variable(tf.random_uniform([decoder_hidden_units, vocab_size], -1, 1), dtype=tf.float32)
b = tf.Variable(tf.zeros([vocab_size]), dtype=tf.float32)


assert EOS == 1 and PAD == 0

eos_time_slice = tf.ones([batch_size], dtype=tf.int32, name='EOS')
pad_time_slice = tf.zeros([batch_size], dtype=tf.int32, name='PAD')

eos_step_embedded = tf.nn.embedding_lookup(embeddings, eos_time_slice)
pad_step_embedded = tf.nn.embedding_lookup(embeddings, pad_time_slice)


# Now for the tricky part.
# 
# Remember that standard `tf.nn.dynamic_rnn` requires all inputs `(t, ..., t+n)` be passed in advance as a single tensor. "Dynamic" part of its name refers to the fact that `n` can change from batch to batch.
# 
# Now, what if we want to implement more complex mechanic like when we want decoder to receive previously generated tokens as input at every timestamp (instead of lagged target sequence)? Or when we want to implement soft attention, where at every timestep we add additional fixed-len representation, derived from query produced by previous step's hidden state? `tf.nn.raw_rnn` is a way to solve this problem.
# 
# Main part of specifying RNN with `tf.nn.raw_rnn` is *loop transition function*. It defines inputs of step `t` given outputs and state of step `t-1`.
# 
# Loop transition function is a mapping `(time, previous_cell_output, previous_cell_state, previous_loop_state) -> (elements_finished, input, cell_state, output, loop_state)`. It is called *before* RNNCell to prepare its inputs and state. Everything is a Tensor except for initial call at time=0 when everything is `None` (except `time`).
# 
# Note that decoder inputs are returned from the transition function but passed into it. You are supposed to index inputs manually using `time` Tensor.

# Loop transition function is called two times:
#  1. Initial call at time=0 to provide initial cell_state and input to RNN.
#  2. Transition call for all following timesteps where you define transition between two adjacent steps.
# 
# Lets define both cases separately.

# Loop initial state is function of only `encoder_final_state` and embeddings:



# =============================================================================
# # method 1: use raw_rnn
# def loop_fn_initial():
#     initial_elements_finished = (0 >= decoder_lengths)  # all False at the initial step
#     initial_input = eos_step_embedded
#     initial_cell_state = encoder_final_state
#     initial_cell_output = None
#     initial_loop_state = None  # we don't need to pass any additional information
#     return (initial_elements_finished,
#             initial_input,
#             initial_cell_state,
#             initial_cell_output,
#             initial_loop_state)
# 
# def loop_fn_transition(time, previous_output, previous_state, previous_loop_state):
# 
#     def get_next_input():
#         output_logits = tf.add(tf.matmul(previous_output, W), b)
#         prediction = tf.argmax(output_logits, axis=1)
#         next_input = tf.nn.embedding_lookup(embeddings, prediction)
#         return next_input
#     
#     elements_finished = (time >= decoder_lengths) # this operation produces boolean tensor of [batch_size]
#                                                   # defining if corresponding sequence has ended
# 
#     finished = tf.reduce_all(elements_finished) # -> boolean scalar
#     input = tf.cond(finished, lambda: pad_step_embedded, get_next_input)
#     state = previous_state
#     output = previous_output
#     loop_state = None
# 
#     return (elements_finished, 
#             input,
#             state,
#             output,
#             loop_state)
# 
# 
# def loop_fn(time, previous_output, previous_state, previous_loop_state):
#     if previous_state is None:    # time == 0
#         assert previous_output is None and previous_state is None
#         return loop_fn_initial()
#     else:
#         return loop_fn_transition(time, previous_output, previous_state, previous_loop_state)
# 
# decoder_outputs_ta, decoder_final_state, _ = tf.nn.raw_rnn(decoder_cell, loop_fn)
# 
# 
# decoder_outputs = decoder_outputs_ta.stack()
# =============================================================================

# method 2: use seq2seq
# 传给CustomHelper的三个函数
def initial_fn():
    initial_elements_finished = (0 >= decoder_lengths)  # all False at the initial step
    initial_input = eos_step_embedded
    return initial_elements_finished, initial_input

def sample_fn(time, outputs, state):
    # 选择logit最大的下标作为sample
    outputs = tf.matmul(outputs, W) + b
    prediction_id = tf.to_int32(tf.argmax(outputs, axis=1))
    return prediction_id

def next_inputs_fn(time, outputs, state, sample_ids):
    # 上一个时间节点上的输出类别，获取embedding再作为下一个时间节点的输入
    next_input = tf.nn.embedding_lookup(embeddings, sample_ids)
    # check BasicDecoder and dynamic_decode, since initial_time is set to 0 at the beginning, so we do time + 1
    elements_finished = (time + 1 >= decoder_lengths)  # this operation produces boolean tensor of [batch_size]
    all_finished = tf.reduce_all(elements_finished)  # -> boolean scalar
    next_inputs = tf.cond(all_finished, lambda: pad_step_embedded, lambda: next_input)
    next_state = state
    return elements_finished, next_inputs, next_state

my_helper = tf.contrib.seq2seq.CustomHelper(initial_fn, sample_fn, next_inputs_fn)


decoder = tf.contrib.seq2seq.BasicDecoder(
        cell=decoder_cell,
        helper=my_helper,
        initial_state=encoder_final_state)

decoder_outputs, decoder_final_state, _ = tf.contrib.seq2seq.dynamic_decode(
        decoder=decoder,
        output_time_major=True)

decoder_outputs = decoder_outputs.rnn_output


decoder_max_steps, decoder_batch_size, decoder_dim = tf.unstack(tf.shape(decoder_outputs))
decoder_outputs_flat = tf.reshape(decoder_outputs, (-1, decoder_dim))
decoder_logits_flat = tf.add(tf.matmul(decoder_outputs_flat, W), b)
decoder_logits = tf.reshape(decoder_logits_flat, (decoder_max_steps, decoder_batch_size, vocab_size))


decoder_prediction = tf.argmax(decoder_logits, 2)

stepwise_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
    labels=tf.one_hot(decoder_targets, depth=vocab_size, dtype=tf.float32),
    logits=decoder_logits
)

loss = tf.reduce_mean(stepwise_cross_entropy)
train_op = tf.train.AdamOptimizer().minimize(loss)

sess.run(tf.global_variables_initializer())

batch_size = 100

batches = helpers.random_sequences(length_from=3, length_to=8,
                                   vocab_lower=2, vocab_upper=10,
                                   batch_size=batch_size)


def next_feed():
    batch = next(batches)
    encoder_inputs_, encoder_input_lengths_ = helpers.batch(batch)
    decoder_targets_, _ = helpers.batch(
        [(sequence) + [EOS] + [PAD] * 2 for sequence in batch]
    )
    return {
        encoder_inputs: encoder_inputs_,
        encoder_inputs_length: encoder_input_lengths_,
        decoder_targets: decoder_targets_,
    }

loss_track = []

max_batches = 3001
batches_in_epoch = 1000

try:
    for batch in range(max_batches):
        fd = next_feed()
        _, l = sess.run([train_op, loss], fd)
        loss_track.append(l)

        if batch == 0 or batch % batches_in_epoch == 0:
            print('batch {}'.format(batch))
            print('  minibatch loss: {}'.format(sess.run(loss, fd)))
            predict_ = sess.run(decoder_prediction, fd)
            for i, (inp, pred) in enumerate(zip(fd[encoder_inputs].T, predict_.T)):
                print('  sample {}:'.format(i + 1))
                print('    input     > {}'.format(inp))
                print('    predicted > {}'.format(pred))
                if i >= 2:
                    break
            print()

except KeyboardInterrupt:
    print('training interrupted')

import matplotlib.pyplot as plt
plt.plot(loss_track)
print('loss {:.4f} after {} examples (batch_size={})'.format(loss_track[-1], len(loss_track)*batch_size, batch_size))

