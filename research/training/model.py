import tensorflow as tf
from tensorflow import keras

from research.loading.load import load_x_y
from research.loading.numpifying import numpify

tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


def train():
    x_train, y_train, x_test, y_test = load_x_y()
    y_train_hot = keras.utils.to_categorical(y_train)
    # print(x_train)
    # print(y_train)
    y_test_hot = keras.utils.to_categorical(y_test)
    model = keras.models.Sequential([
        keras.layers.Flatten(input_shape=x_train[0].shape),
        keras.layers.Dense(6, activation=tf.nn.softmax)
    ])
    model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train_hot, epochs=100)
    result = model.evaluate(x_test, y_test_hot)
    # model.save_weights('model.h5')
    model.save('model.h5')
    print(result)


