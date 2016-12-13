from fakultaet import f
from math import factorial
from os import stat

print(stat("fakultaet.py").st_size)

for n in range(10):
	if factorial(n)!=f(n) or type(f(n))==bool:
		print n, f(n), factorial(n)
