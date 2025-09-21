import numpy as np

# Ej 3
A = np.array([
    [1,2,-1,0],
    [2,3,1,6],
    [0,1,0,1]
])

S = A @ A.transpose()
eva, eve = np.linalg.eig(S)
print(eva)

S = A.transpose() @ A
eva, eve = np.linalg.eig(S)
print(eva)

# Ej 7
A = np.array([
    [1,2,-1,0],
    [2,3,1,6],
    [0,1,0,1]
])
Astar = np.linalg.pinv(A)
x = np.array([1,2,3])
print(Astar @ x)
