import numpy as np

A = np.array([[1,2,3,4,5,6], [3,4,5,6,7,8]])
B = np.array([[5,6,4,5,6,4], [7,8,9,10,11,12]])

C = np.dot(A, B.T)

print(C)