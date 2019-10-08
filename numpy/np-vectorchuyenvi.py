import numpy as np

# Tao ma tran a
A = np.array([[1, 2, 3], [4, 5, 6]])

# Chuyen vi cua ma tran A
B = A.transpose()
print(B)

# Phep nhan vo huong 2 ma tran, tong cua tich moi phan tu tuong ung cua 2 ma tran
a = np.arange(10)
print(a)
b = np.ones(10)
print(b)
c = a.dot(b)
print(c)
# 45.0

# Numpy
c = np.inner(a, b)
print(c)
# 45.0