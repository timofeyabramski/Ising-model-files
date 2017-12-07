#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np 

x = np.arange(0.01, 1.00 , 0.01)
listx = np.exp(x)

def V(x):
	return A*np.exp(-x/p) - l/x
l = 1.44
A=1090.
p=0.033

def dV(x):
	return -(A/p)*np.exp(-x/p) +l/(x**2)
def ddV(x):
	return (A/p**2)*np.exp(-x/p) - 2*l/x**3

t=np.arange(0.01,1,0.01)
plt.plot(t,ddV(t))
plt.title('x vs second derivative of V(x)')
plt.ylabel('second derivative of V(x)')
plt.xlabel('x')
x1= float(raw_input("Enter x1: "))
tol = 0.0001
while abs(dV(x1))>tol:
	x1=x1 - (dV(x1)/ddV(x1))
	print x1, V(x1)
print V(0.23605)




