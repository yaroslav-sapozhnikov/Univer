import numpy as np

lam = 32
mu = 5
m = 7
n = 5
L = np.zeros((m+n+1, m+n+1))
for i in range(m+n+1):
    for j in range(m+n+1):
        if j - i == 1:
            L[i, j] = lam
        if i - j == 1:
            if j < m:
                L[i, j] = (i + 1) * mu
            else:
                L[i, j] = m * mu

print(L)
