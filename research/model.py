import tensorflow as tf
from tensorflow import keras

from research.load import load_x_y
from research.numpifying import numpify

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


def predict_tag(text):
    x, y = numpify([{'body': text, 'tag': 'unknown'}])
    model = keras.models.load_model('/home/ms10596/Documents/match/research/model.h5')
    list_of_probabilities = model.predict(x)
    return tags[list_of_probabilities.argmax()]


# train()
# print(predict_tag("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
# What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
# she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
# fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
# asked her. "No," she said, "now my left arm hurts a lot."""""))
