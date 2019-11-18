import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
#import pandas as pd 


def app():
    data = loadmat('data_preg.mat').get('data')
    #data = pd.read_csv("data_preg.csv") 

    x = []
    y = []
    for i in range(len(data)):
        x.append(data[i][0])
        y.append(data[i][1])

    z = np.polyfit(x, y, 5)
    p = np.poly1d(z)
    plt.scatter(x, y)
    plt.plot(p)
    plt.show()

app()