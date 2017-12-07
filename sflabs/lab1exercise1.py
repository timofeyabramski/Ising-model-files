


#!/usr/bin/python 
import matplotlib.pylab as plt
import numpy as np 


def p(x):
    return x**2 + 2*x -100 #defined the function

t=np.arange(-15,15,0.01) #restricted domain
plt.plot(t,p(t))
z=np.arange(-15,15,0.001)
plt.plot(z, 0.0* z)    

plt.plot([-2,-3,-4,-5,-6], [12,17,19,24,27])
plt.show()

x1= float(raw_input("Enter x1: "))
x3= float(raw_input("Enter x3: "))
x1=0 #f(x1)<0 #chose starting points

if p(x3)>0 and p(x1)>0:
      print 'BAD CHOICE OF VARIABLES'
if p(x3)<0 and p(x1)<0: 
      print 'BAD CHOICE OF VARIABLES' #give warning sign if bad variables
x2=(x1+x3)/2

#setting tolerance number
tol = 0.01
 
#count
counter=1
while abs(p(x2)) > tol:
	if p(x2)>0:
		x3=x2
	else:
		x1=x2
	x2=(x1+x3)/2
	counter = counter+1
	print counter,x1, x2, x3, p(x2)
plt.plot(x2,p(x2),'g^')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('f(x)=x^2 + 2x - 100')






