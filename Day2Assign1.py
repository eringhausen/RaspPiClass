#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
for t in range(1,3):
    y=6*np.log(t)-7*np.exp(0.2*t)
    print (y)
    plt.plot(t, y)
    plt.xlabel('time')
    plt.ylabel('Temperature (Celcius)')
    plt.title('Elizabeth Ringhausen')
'plt.show()'
print('Hello World! I just wrote my first Python program.  Yayyyyyyyy                  Elizabeth Ringhausen') 

