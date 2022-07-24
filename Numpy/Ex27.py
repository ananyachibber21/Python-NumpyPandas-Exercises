import numpy as np
A = np.zeros(shape=(6, 6), dtype='int')
A[::2, ::2] = 10
A[1::2, ::2] = 5
print(A)
