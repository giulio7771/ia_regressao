import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.model_selection import train_test_split

def app():
    data = loadmat('data_preg.mat').get('data')
    #data = pd.read_csv("data_preg.csv") 
    data_x, x_test = train_test_split(data, test_size=0.1)

    x = []
    y = []
    for i in range(len(data_x)):
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

def eqm(y, y_):
    pass


app()