#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np 

def f(x):
    return x**2 + 2*x -100

def df(x):
	return 2*x + 2

x1= float(raw_input("Enter x1: "))
x1=x1 - f(x1)/df(x1)
print x1
t=np.arange(-30,30,0.01)
plt.plot(t,f(t))
plt.plot(x1,f(x1),'g^')
plt.show()
tol = 0.000001
while abs(f(x1))>tol:
	x1=x1 - (f(x1)/df(x1))
	print x1



