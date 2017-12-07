#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np
import math


g=1
L=1
k=0.0
A=0.0
fi=0.66667
theta= 0.0
omega = 1.0
t = 0.0
dt = 0.01
nsteps = 0 

def f(theta, omega, t):
	force= -(g/L)*math.sin(theta)-k*omega + A*math.cos(fi*t)
	return force

ltheta = [theta]
lomega = [omega]
lt=[t]

#trap rule
for nn in range(1000):
	k1a = dt * omega 
	k1b = dt * f(theta, omega, t) 
	k2a = dt * (omega + k1b)
	k2b = dt * f(theta + k1a, omega + k1b, t + dt)
	theta = theta + (k1a + k2a) / 2 
	omega = omega + (k1b + k2b) / 2 
	t = t + dt     
   
	ltheta.append(theta)
	lomega.append(omega)
	lt.append(t)	
plt.plot(lt,ltheta, 'ro-')
plt.plot(lt, lomega, 'bs-')
plt.xlabel('Time')
plt.ylabel('Omega(red), Theta(blue)')
plt.grid(True)
plt.title('Nonlinear pendelum, theta starting at 0.0, omega at 1.0')
plt.show()


