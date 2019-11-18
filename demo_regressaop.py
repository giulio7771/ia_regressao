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

    p1 = np.polyfit(x, y, 1)
    p2 = np.polyfit(x, y, 2)
    p3 = np.polyfit(x, y, 3)
    p8 = np.polyfit(x, y, 8)
    plt.scatter(x, y)
    plt.plot(x, np.polyval(p1, x), 'r-')
    plt.plot(x, np.polyval(p2, x), 'g-')
    plt.plot(x, np.polyval(p3, x), 'b-')
    plt.plot(x, np.polyval(p8, x), 'y-')
    plt.show()

app()