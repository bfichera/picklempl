import pickle

from matplotlib import pyplot as plt


def dump(filename):
    fig = plt.gcf()
    with open(filename, 'wb') as fh:
        pickle.dump(fig, fh)


def plot(filename):
    with open(filename, 'rb') as fh:
        fig = pickle.load(fh)
    plt.show()


def load(filename):
    with open(filename, 'rb') as fh:
        fig = pickle.load(fh)
    return fig
