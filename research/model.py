import tensorflow as tf
from tensorflow import keras

from research.loading import Load

tags = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


class Model:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def train(self):
        self.y = keras.utils.to_categorical(self.y)
        model = keras.models.Sequential([
            keras.layers.Flatten(input_shape=self.x[0].shape),
            keras.layers.Dense(6, activation=tf.nn.softmax)
        ])
        model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(self.x, self.y, epochs=100)
        result = model.evaluate(self.x, self.y)
        print(result)
        # model.save('model.h5')


x, y = Load.load()
Model(x, y).train()
