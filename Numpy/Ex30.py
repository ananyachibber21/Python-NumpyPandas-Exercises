import numpy as np
np.random.seed(10)
A = np.random.randint(low=1, high=10, size=(3, 5))
print(np.unique(A))
