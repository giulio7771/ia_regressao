from q1 import plot

def app():
    x1 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    plot(x1, y1)

    x2 = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y2 = [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    plot(x2, y2)

    #dataset impróprio para o uso de regressão
    x3 = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19]
    y3 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56,7.91, 6.89, 12.50]
    plot(x3, y3)

app()