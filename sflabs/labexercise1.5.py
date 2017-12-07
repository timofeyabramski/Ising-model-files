import matplotlib.pylab as plt
import numpy as np 

plt.plot([-2,-3,-4,-5,-6], [12,17,19,24,27])
plt.title('graph of log of tol vs nsteps')
plt.xlabel('log base 10 of tol value')
plt.ylabel('# of steps taken')
plt.show()
