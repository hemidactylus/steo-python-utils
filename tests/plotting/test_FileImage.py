import matplotlib.pyplot as plt

from steoutils.plotting import FileImage

with FileImage('plot1.png', 10, 4) as fi:
    plt.plot([1, 2, 3], [10, 11, 9], '*-')
    plt.title('Plot Title')
