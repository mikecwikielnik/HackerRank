import numpy as np



n,m = list(map(int, input().split()))
arr = np.array([input().split() for i in range(n)], int)
a = arr.T
print(a)
b = arr.flatten()
print(b)
