import numpy as np
A = np.arange(8).reshape(-1,4)
B = np.array([[9,10,11,3],[2,8,0,9]])
print(np.intersect1d(A, B))
