#!/usr/bin/env python
'import matplotlib.pyplot as plt'
from math import exp, log
for t in range(1,3):
    y=6*log(t)-7*exp(0.2*t)
    print (y)
    'plt.plot(t, y)'
'plt.show()'
