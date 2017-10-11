import tensorflow as tf

# using Tensorflow practice data
# It uses handwritten images of 0 - 9, then learns to read them based on the data set 
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("data", one_hot=True) # 'one_hot' refers to whether the data is 'on' or 'off' 


n_nodes_hl1 = 500  # Hidden Layers, these can be different values
n_nodes_hl2 = 500
n_nodes_hl3 = 500

# 10 classes, 0-9
n_classes = 10
batch_size = 100 # Pushing data through the network in batches of 100


# height x width
# the images are 28x28 pixels, 
x = tf.placeholder('float', [None, 784])  # Input data is changed to have height of 0 and length of 784
# 784 because 28 * 28 = 784

y = tf.placeholder('float')  # Output data


def neural_network_model(data):

    # Defining weights & biases as Tensors, with random values
    hidden_1_layer = {'weights': tf.Variable(tf.random_normal([784, n_nodes_hl1])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl1]))}

    hidden_2_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl2]))}

    hidden_3_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl2, n_nodes_hl3])),
                      'biases': tf.Variable(tf.random_normal([n_nodes_hl3]))}

    output_layer = {'weights': tf.Variable(tf.random_normal([n_nodes_hl3, n_classes])),
                      'biases': tf.Variable(tf.random_normal([n_classes]))}

    # (input_data * weights) + biases

    l1 = tf.add(tf.matmul(data, hidden_1_layer['weights']), hidden_1_layer['biases'])
    l1 = tf.nn.relu(l1)  # Activation function

    l2 = tf.add(tf.matmul(l1, hidden_2_layer['weights']), hidden_2_layer['biases'])
    l2 = tf.nn.relu(l2)  # Activation function

    l3 = tf.add(tf.matmul(l2, hidden_3_layer['weights']), hidden_3_layer['biases'])
    l3 = tf.nn.relu(l3)  # Activation function

    output = tf.matmul(l3, output_layer['weights']) + output_layer['biases']

    return output


def train_neural_network(x):
    # this is the 'trainer' 
    # Calculates the cost, then optimizes it
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=y))
    optimizer = tf.train.AdamOptimizer().minimize(cost)


    # Epochs are cycles of feed foward + back propigation
    hm_epochs = 10  # How many epochs do we want?

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables()) # could be changed to tf.global_variables_initializer?

        for epoch in range(hm_epochs):
            epoch_loss = 0
            for _ in range(int(mnist.train.num_examples / batch_size)):
                epoch_x, epoch_y = mnist.train.next_batch(batch_size)
                _, c = sess.run([optimizer, cost], feed_dict={x: epoch_x, y: epoch_y})
                epoch_loss += c
            print('Epoch', epoch, 'completed out of', hm_epochs, 'loss', epoch_loss)

        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))

        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        print('Accuracy:', accuracy.eval({x: mnist.test.images, y: mnist.test.labels}))



train_neural_network(x)
