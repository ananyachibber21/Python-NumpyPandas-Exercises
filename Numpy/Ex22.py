import numpy as np
x = np.arange(0,12).reshape(3,4)
np.save('array.npy', x)
y = np.load('array.npy')
print(y)
