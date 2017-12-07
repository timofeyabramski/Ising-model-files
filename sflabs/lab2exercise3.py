#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np
import math


g=1
L=1
k=0.0
A=0.0
fi=0.66667
theta= 3.0 
omega = 0.0
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
	k2a = dt * (omega+k1b/2)
	k2b = dt * f(theta +k1a/2, omega+k1b/2, t+dt/2)
	k3a = dt * (omega + k2b/2)
	k3b = dt * f(theta +k2a/2, omega+k2b/2, t+dt/2)
	k4a = dt * (omega+k3b)
	k4b = dt * f(theta+k3a, omega +k3b, t+dt)
	theta = theta + (k1a + 2*k2a +2*k3a +k4a)/6
	omega = omega + (k1b+ 2*k2b + 2*k3b + k4b)/6
	t = t + dt
	ltheta.append(theta)
	lomega.append(omega)     
	lt.append(t)	
plt.plot(lt,ltheta, 'ro-')
plt.plot(lt, lomega, 'bs-')
plt.xlabel('Time')
plt.ylabel('Omega(red), Theta(blue)')
plt.grid(True)
plt.title('A')
plt.show()


