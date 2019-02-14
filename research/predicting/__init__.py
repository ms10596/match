def predict_tag(text):
    x, y = numpify([{'body': text, 'tag': 'unknown'}])
    model = keras.models.load_model('/home/ms10596/Documents/match/research/model.h5')
    list_of_probabilities = model.predict(x)
    return tags[list_of_probabilities.argmax()]


# train()
print(predict_tag("""Lucy went to the doctor. She didn't feel good. The doctor asked, "What's the problem?
What's the matter?" She said she didn't feel right. "Do you hurt? Where do you hurt?" the doctor asked. She said that
she hurt all over. She hurt everywhere. She hurt all over her body. The doctor said, "You have a big problem. I will
fix your problem." The doctor gave Lucy a shot. He gave her a shot in her left arm. "Do you feel better now?" he
asked her. "No," she said, "now my left arm hurts a lot."""""))
