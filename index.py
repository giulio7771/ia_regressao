def correlacao(xv, yv):
	x_ = media(xv)
	y_ = media(yv)
	for i in range(len(xv)):
		k = (xv[i] - x_) * (yv[i] - y_)
	pass

def regressao(xv, yv):
	pass

def media(v):
	soma = 0
	for i in v:
		soma += i
	return soma/len(v) 	