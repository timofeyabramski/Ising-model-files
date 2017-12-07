Useful commands:
plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) will default with blue line
plt.plot([1,2,3,4], [1,4,9,16], 'ro') red circles
plt.axis([0, 6, 0, 20]) defines axis limits
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^') different squares, trianlges etc
plt.plot(x,y, linewidth=10)
 xlabel(), ylabel() and title() 


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()



http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html
