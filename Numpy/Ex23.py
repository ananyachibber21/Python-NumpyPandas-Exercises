import numpy as np
x = np.arange(0,12).reshape(3,4)
np.savetxt('array.txt', x, fmt='%0.2f')
y = np.loadtxt('array.txt')
print(y)
