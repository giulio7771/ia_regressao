import matplotlib.pyplot as plt
import math

b0 = 0
b1 = 0

def correlacao(xv, yv):
	x_ = media(xv)
	y_ = media(yv)
	up = 0
	soma_x = 0
	soma_y = 0
	for i in range(len(xv)):
		x_med = (xv[i] - x_)
		y_med = (yv[i] - y_)
		up +=  x_med * y_med 
		soma_x += x_med ** 2
		soma_y += y_med ** 2
	down = (soma_x * soma_y) ** 0.5
	return up / down 

def regressao(xv, yv):
	b0, b1 = betas(xv, yv)
	y_ = []
	for i in range(len(xv)):
		x = xv[i]
		y_.append(b0 + b1 * x)
	return y_

def betas(xv, yv):
	global b0, b1
	b0 = 0
	b1 = 0
	b1_up = 0
	b1_down = 0
	x_ = media(xv)
	y_ = media(yv)
	for i in range(len(xv)):
		x_med = (xv[i] - x_)
		y_med = (yv[i] - y_)
		b1_up +=  (x_med * y_med)
		b1_down += (x_med ** 2)
	b1 = b1_up / b1_down
	b0 = y_ - b1 * x_
	return [b0, b1]

def media(v):
	soma = 0
	for i in v:
		soma += i
	return soma / len(v)

def plot(x, y):
	global b0, b1
	cor = correlacao(x, y)
	y_ = regressao(x, y)
	plt.scatter(x, y)
	plt.plot(x, y_)
	plt.title('Correlação: {}'.format(truncate(cor,2)), loc = 'left')
	plt.title('B0: {}'.format(truncate(b0,5)), loc = 'center')
	plt.title('B1: {}'.format(truncate(b1,5)), loc = 'right')
	plt.show()

def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def app():
	x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
	y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
	plot(x, y)

#app()