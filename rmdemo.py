from scipy.io import loadmat
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from q1 import correlacao

B = 0
def getLinha(matriz, n):
    return [i for i in matriz[n]]

def getColuna(matriz, n):
    return [i[n] for i in matriz]

def matrix_mult(X, Y):
    X_len = len(X)
    Y_column_len = len(Y[0])

    Z = []
    for i in range(X_len):           
        Z.append([])
        for j in range(Y_column_len):
            listMult = [x*y for x, y in zip(getLinha(X, i), getColuna(Y, j))]
            Z[i].append(sum(listMult))
    return Z

def regmultipla(X, y):
    global B
    B = beta(X, y)
    y_ = np.dot(X, B)
    return y_

def beta(X, y):
    Xt = np.transpose(X)
    part1 = np.dot(Xt, X)
    inverse_part1 = np.linalg.inv(part1)
    part2 = np.dot(Xt, y)
    return np.dot(inverse_part1, part2)

def transposta(X):
    Xt = []
    for i in range(len(X[0])):
        nova_linha = []
        for j in range(len(X)):
            nova_linha.append(X[j][i])
        Xt.append(nova_linha)
    return Xt


def app():
    #tamanho da casa, número de quartos, preço
    data = loadmat('data.mat').get('data')
    y = []
    X = []
    for i in range(len(data)):
        y.append(data[i][2])
        X.append([1, data[i][0], data[i][1]])
    y_ = regmultipla(X, y)
    
    tamanho_casa = []
    n_quartos = []
    preco = []
    for i in range(len(X)):
        tamanho_casa.append(X[i][1])
        n_quartos.append(X[i][2])
        preco.append(y_[i])
    
    
    cor_tamanho = correlacao(tamanho_casa, y)
    cor_quartos = correlacao(n_quartos, y)
    print("correlacao tamanho da casa: {}".format(cor_tamanho))
    print("correlacao numero de quartos: {}".format(cor_quartos))
    
    fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    ax = plt.axes(projection='3d')

    #for i in range(len(X)):
    #    tamanho_casa.append(X[i][1])
    #    n_quartos.append(X[i][2])
    #ax.plot_wireframe(tamanho_casa, n_quartos, y_, rstride=15, cstride=15)
    
        #ax.plot3D(tamanho_casa, n_quartos, preco, 'gray')
    ax.plot3D(tamanho_casa, n_quartos, preco, 'gray')
    
    # Exibindo o gráfico criado
    plt.show()
    


app()