import matplotlib.pyplot as plt

from research.loading import Load

x, y = Load.load()
pos_tags = Load.load_pos_tags()
print(len(pos_tags))
i=0
for key in pos_tags:
    plt.title(key)
    plt.plot(x[:, i], y, 'go')
    i = i+1
    plt.show()
