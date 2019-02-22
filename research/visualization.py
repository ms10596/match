import matplotlib.pyplot as plt

from research.loading import load, load_pos_tags, load_reduced_features_tags

x, y = load()
pos_tags = load_reduced_features_tags()
print(len(pos_tags))
i=0
for key in pos_tags:
    plt.title(key)
    plt.plot(x[:, i], y, 'go')
    i = i+1
    plt.show()
