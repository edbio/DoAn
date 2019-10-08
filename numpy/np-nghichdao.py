import numpy as np

# Tao ma tran a
A = np.array([[1., 2.], [3., 4.]])

# Nghich dao cua ma tran A
B = np.linalg.inv(A)
print(B)