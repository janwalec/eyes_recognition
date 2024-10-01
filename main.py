import numpy as np

n = 2000
m = 2

arr = np.zeros((n, m), dtype=int)
arr[:, 0] = np.arange(n)

print(arr)