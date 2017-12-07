#!/usr/bin/python 
import matplotlib
matplotlib.use('Tkagg')


import matplotlib.pylab as plt
import numpy as np 



x=np.arange(1,4,1)
y=np.arange(1,7,2)
plt.axis([1,3, 1, 5])
line = plt.plot(x, y, '-')
plt.show()
