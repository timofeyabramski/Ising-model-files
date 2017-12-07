#!/usr/bin/env python


#module that saves matrix as .pbm file

import numpy as np


def savefunction(x):
	np.savetxt('f',x, fmt='%i')


