import numpy as np

A = np.array([[3, 2, 1, 4],
              [5, 2, 1, 6]])

B = np.array([[3, 2, 1, 4],
              [5, 2, 0, 6]])

C = np.array([[True, False, False],
              [True, True, True]])

D = np.array([0.1, 0.3])

list1 = [A,B,C,D]
for letter, value in zip(list('ABCD'), list1):
    print(f"{letter}: {np.all(value)}")
