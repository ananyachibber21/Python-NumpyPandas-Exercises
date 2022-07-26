import numpy as np
A = np.arange(12).reshape(-1,4)
B = np.array([[4,3,7,2],[0,5,2,6]])
print(np.append(A, B, axis=0))
