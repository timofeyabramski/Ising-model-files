#!/usr/bin/env python

import mymod
import numpy as np
import matplotlib.pyplot as plt



n=20
m=20

A=np.random.random_sample(n*m).reshape(n,m)
B=np.rint(A)

mymod.savefunction(B)

plt.imshow(B)
