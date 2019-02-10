import tensorflow as tf
from tensorflow import keras

from load import load_x_y

x_train, y_train, x_test, y_test = load_x_y()
y_train_hot = keras.utils.to_categorical(y_train)
y_test_hot = keras.utils.to_categorical(y_test)
model = keras.models.Sequential([
    keras.layers.Flatten(),
    keras.layers.Dense(6, activation=tf.nn.softmax)
])
model.compile(optimizer='sgd', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=10)
result = model.evaluate(x_test, y_test_hot)
print(result)
