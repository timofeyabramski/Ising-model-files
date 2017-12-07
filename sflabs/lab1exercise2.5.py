#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np 

plt.plot([-2,-3,-4,-5,-6], [4,4,5,5,6])
plt.title('graph of log of tol value vs no. of steps')
plt.ylabel('no. of steps')
plt.xlabel('log of tol value')
plt.show()
