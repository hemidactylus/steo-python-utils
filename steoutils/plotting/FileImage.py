import matplotlib.pyplot as plt

class FileImage():
    def __init__(self, fname, x, y, verbose=True):
        # if fname = None, this is taken as a 'show-on-exit' thing
        self.fname = fname
        self.verbose = verbose
        self.fig = plt.figure(figsize=(x, y))

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        if self.fname is not None:
            # save the figure and close it
            self.fig.savefig(self.fname, bbox_inches='tight')
            if self.verbose:
                print(f'[FileImage] Saving "{self.fname}"')
            plt.close(self.fig)
        else:
            plt.show()
            plt.close(self.fig)
