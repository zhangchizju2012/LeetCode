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
decoder_hidden_units = encoder_hidden_units

encoder_inputs = tf.placeholder(shape=(None, None), dtype=tf.int32, name='encoder_inputs')
decoder_targets = tf.placeholder(shape=(None, None), dtype=tf.int32, name='decoder_targets')

decoder_inputs = tf.placeholder(shape=(None, None), dtype=tf.int32, name='decoder_inputs')


embeddings = tf.Variable(tf.random_uniform([vocab_size, input_embedding_size], -1.0, 1.0), dtype=tf.float32)

encoder_inputs_embedded = tf.nn.embedding_lookup(embeddings, encoder_inputs)
decoder_inputs_embedded = tf.nn.embedding_lookup(embeddings, decoder_inputs)

encoder_cell = tf.contrib.rnn.LSTMCell(encoder_hidden_units)

encoder_outputs, encoder_final_state = tf.nn.dynamic_rnn(
    encoder_cell, encoder_inputs_embedded,
    dtype=tf.float32, time_major=True,
)

del encoder_outputs

decoder_cell = tf.contrib.rnn.LSTMCell(decoder_hidden_units)

# =============================================================================
# # method 1: use dynamic_rnn
# decoder_outputs, decoder_final_state = tf.nn.dynamic_rnn(
#     decoder_cell, decoder_inputs_embedded,
# 
#     initial_state=encoder_final_state,
# 
#     dtype=tf.float32, time_major=True, scope="plain_decoder",
# )
# =============================================================================

# method 2: use seq2seq
decoder_inputs_length = tf.placeholder(shape=(None,), dtype=tf.int32, name='decoder_inputs_length')

helper = tf.contrib.seq2seq.TrainingHelper(
        inputs=decoder_inputs_embedded,
        sequence_length=decoder_inputs_length,
        time_major=True)

decoder = tf.contrib.seq2seq.BasicDecoder(
        cell=decoder_cell,
        helper=helper,
        initial_state=encoder_final_state)

decoder_outputs, decoder_final_state, _ = tf.contrib.seq2seq.dynamic_decode(
        decoder=decoder,
        output_time_major=True)#,
        #impute_finished=True)
        
decoder_outputs = decoder_outputs.rnn_output

#decoder_logits = tf.contrib.layers.linear(decoder_outputs, vocab_size)

he_normal = tf.keras.initializers.he_normal()
# tf.matmul 有坑
decoder_max_steps, decoder_batch_size, decoder_dim = tf.unstack(tf.shape(decoder_outputs))
decoder_outputs = tf.reshape(decoder_outputs, (-1, decoder_dim)) # or decoder_hidden_units
with tf.variable_scope("fully-connected"):
    W = tf.get_variable('W', [decoder_hidden_units, vocab_size], initializer=he_normal)
    b = tf.get_variable('b', [vocab_size], initializer=tf.constant_initializer(0.0))
    decoder_logits = tf.matmul(decoder_outputs, W) + b
decoder_logits = tf.reshape(decoder_logits, (decoder_max_steps, decoder_batch_size, vocab_size))

decoder_prediction = tf.argmax(decoder_logits, 2)


stepwise_cross_entropy = tf.nn.softmax_cross_entropy_with_logits(
    labels=tf.one_hot(decoder_targets, depth=vocab_size, dtype=tf.float32),
    logits=decoder_logits,
)

loss = tf.reduce_mean(stepwise_cross_entropy)
train_op = tf.train.AdamOptimizer().minimize(loss)


sess.run(tf.global_variables_initializer())

batch_size = 100

batches = helpers.random_sequences(length_from=3, length_to=8,
                                   vocab_lower=2, vocab_upper=10,
                                   batch_size=batch_size)

# =============================================================================
# def next_feed():
#     batch = next(batches)
#     encoder_inputs_, _ = helpers.batch(batch)
#     decoder_targets_, _ = helpers.batch(
#         [(sequence) + [EOS] for sequence in batch]
#     )
#     decoder_inputs_, _ = helpers.batch(
#         [[EOS] + (sequence) for sequence in batch]
#     )
#     return {
#         encoder_inputs: encoder_inputs_,
#         decoder_inputs: decoder_inputs_,
#         decoder_targets: decoder_targets_,
#     }
# 
# =============================================================================
def next_feed():
    batch = next(batches)
    encoder_inputs_, encoder_input_lengths_ = helpers.batch(batch)
    decoder_targets_, _ = helpers.batch(
        [(sequence) + [EOS] for sequence in batch]
    )
    decoder_inputs_, _ = helpers.batch(
        [[EOS] + (sequence) for sequence in batch]
    )
    decoder_input_lengths_ = [value + 1 for value in encoder_input_lengths_]
    
    return {
        encoder_inputs: encoder_inputs_,
        decoder_inputs: decoder_inputs_,
        decoder_targets: decoder_targets_,
        decoder_inputs_length: decoder_input_lengths_,
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

