import matplotlib.pyplot as plt

class FileImage():
    def __init__(self, fname, x, y):
        self.fname = fname
        self.fig = plt.figure(figsize=(x, y))

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        # save the figure and close it
        self.fig.savefig(self.fname, bbox_inches='tight')
        plt.close(self.fig)
