import matplotlib.pyplot as plt

from steoutils.plotting import FileImage

with FileImage('plot1.png', 10, 4) as fi:
    plt.plot([1, 2, 3], [10, 11, 9], '*-')
    plt.title('Plot Title')


with FileImage(None, 10, 4) as fi:
    plt.plot([10, 20, 30], [100, 110, 90], ':')
    plt.title('To go on screen only')
