#!/usr/bin/env python
import matplotlib as plt
import numpy as np
import scipy as scipy


def f(x):
	return np.exp(pow(x-0.7,2))
scipy.optimize.minimize_scalar(f)

