import matplotlib.pyplot as plt

from research.loading import Load

x, y = Load.load()
print(x[:, 0].shape)
features = ['avg_sentece_length', 'avg word length', 'adj', 'adv', 'article', 'conjunctions', 'interjection', 'nouns', 'numerals', 'past participle', 'pronouns', 'symbols']
for i in range(12):
    plt.title(features[i])
    plt.plot(x[:, i], y, 'go')
    plt.show()
