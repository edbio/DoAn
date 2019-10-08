import numpy as np

# Tao ma tran a
a = np.array([(1, 2, 3), (4, 5, 6)])
print(a)


# Tao ma tran b
b = np.array([(0, 5, 25), (4, 9, 9)])
print(b)
# [[0 5 25]
#  [4 9  9]]

# Cong ma tran a voi ma tran b
c = a + b
print(c)

c = np.add(a, b)
print(c)

# Tru ma tran a voi ma tran b
c = np.subtract(a, b)
print(c)

c = a - b
print(c)