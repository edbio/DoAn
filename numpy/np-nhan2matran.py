import numpy as np

# Tao ma tran A
A = np.array([(1, 2, 3), (4, 5, 6)])
print(A)

# Tao ma tran B
B = np.array([(0, 5), (4, 9), (9, 0)])
print(B)

# Nhan 2 ma tran A va B

# Khong dung numpy
C = A.dot(B)
print(C)
# [[35 23]
#  [74 65]]

# Numpy
C = np.dot(A, B)
print(C)