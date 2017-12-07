#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np
import math

it_nu=1
tra = 5000
g=1
L=1
k=0.5
A=0.9
fi=0.66667
theta= 3.0 
omega = 0.0
t = 0.0
dt = 0.01
nsteps = 0 

def f(theta, omega, t):
	force= -(g/L)*math.sin(theta)-k*omega + A*math.cos(fi*t)
	return force

ltheta = []
lomega = []
lt=[]

#trap rule
while it_nu<10000:
	k1a = dt * omega 
	k1b = dt * f(theta, omega, t) 
	k2a = dt * (omega + k1b)
	k2b = dt * f(theta + k1a, omega + k1b, t + dt)
	theta = theta + (k1a + k2a) / 2 
	omega = omega + (k1b + k2b) / 2 
	t = t + dt
	it_nu=it_nu +1
        if it_nu >5000:
       		ltheta.append(theta)
		lomega.append(omega)
		lt.append(t)
	
plt.plot(ltheta,lomega, 'ro-')
plt.xlabel('Time')
plt.ylabel('Omega(red), Theta(blue)')
plt.grid(True)
plt.title('')
plt.show()


