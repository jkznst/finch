from rnn_text_clf import RNNTextClassifier
import tensorflow as tf
import numpy as np


max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32


if __name__ == '__main__':
    print('Loading data...')
    (X_train, y_train), (X_test, y_test) = tf.contrib.keras.datasets.imdb.load_data(num_words=max_features)
    print(len(X_train), 'train sequences')
    print(len(X_test), 'test sequences')

    print('Pad sequences (samples x time)')
    X_train = tf.contrib.keras.preprocessing.sequence.pad_sequences(X_train, maxlen=maxlen)
    X_test = tf.contrib.keras.preprocessing.sequence.pad_sequences(X_test, maxlen=maxlen)
    print('x_train shape:', X_train.shape)
    print('x_test shape:', X_test.shape)
    Y_train = tf.contrib.keras.utils.to_categorical(y_train)
    Y_test = tf.contrib.keras.utils.to_categorical(y_test)

    clf = RNNTextClassifier(maxlen, max_features, 2)
    log = clf.fit(X_train, Y_train, n_epoch=2, batch_size=batch_size, keep_prob_tuple=(1.0,1.0),
                  val_data=(X_test,Y_test), en_exp_decay=False)
    pred = clf.predict(X_test)

    final_acc = np.equal(np.argmax(pred,1), np.argmax(Y_test,1)).astype(float).mean()
    print("final testing accuracy: %.4f" % final_acc)
