def f(n):
	p = 1
	exec("p *= n;n -= 1;"*n)
	return p