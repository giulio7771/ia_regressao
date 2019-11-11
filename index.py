def correlacao(xv, yv):
	x_ = media(xv)
	y_ = media(yv)
	up = 0
	down = 0
	soma_x = 0
	soma_y = 0
	for i in range(len(xv)):
		x_med = (xv[i] - x_)
		y_med = (yv[i] - y_)
		up +=  x_med * y_med 
		soma_x = x_med ** 2
		soma_y = y_med ** 2
	return soma_x * soma_y

def regressao(xv, yv):
	b0, b1 = betas(xv, yv)
	soma_b1_x = 0
	for i in range(len(xv)):
		x = xv[i]
		soma_b1_x += b1 * x
	return b0 + soma_b1_x

def betas(xv, yv):
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
	return soma/len(v)

def app():
	x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
	y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
	cor = correlacao(x, y)
	print(cor)

app()
