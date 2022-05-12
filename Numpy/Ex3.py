import numpy as np

A = np.array([[0, 0, 0],
              [0, 0, 0]])

B = np.array([[0, 0, 0],
              [0, 1, 0]])

C = np.array([[False, False, False],
              [True, False, False]])

D = np.array([[0.1, 0.0]])

list1 = [A,B,C,D]
for letter, value in zip(list('ABCD'), list1):
    print(f"{letter}: {np.any(value)}")
