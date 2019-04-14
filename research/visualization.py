import matplotlib.pyplot as plt

from research.loading import load, load_pos_tags, load_reduced_features_tags, raw

x, y = load()
pos_tags = load_reduced_features_tags()
print(len(pos_tags))
i=0
for key in pos_tags:
    plt.title(key)
    plt.yticks([0, 1, 2, 3, 4, 5],['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
    plt.plot(x[:, i], y, 'go')
    i = i+1
    plt.show()

# articles = raw()
# plt.title('avg word length')
# plt.yticks([0, 1, 2, 3, 4, 5],['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
# plt.plot([i.avg_word_length() for i in articles], [i.category for i in articles], 'go')
# plt.show()