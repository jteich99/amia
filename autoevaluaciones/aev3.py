import numpy as np

# Ejercicio 5
A = np.array([
    [1,3,2],
    [4,2,-1],
    [5,5,1]
])
testAves = [
    np.array([ 1, 0, -1 ]),
    np.array([ 5/3, 1, 8/3 ]),
    np.array([ -1, 1, 0]),
    np.array([ 7, 9, -10]),
    np.array([ 1/np.sqrt(2), - 1/np.sqrt(2), 0]),
    np.array([ -7, 9, -10 ]),
    np.array([ 5/3, 1, 8/3]),
    np.array([ -1, 1, 0])
]

tol = 1e-4
for testAve in testAves:
    newVec = A @ testAve
    if 0 not in testAve:
        if (
            newVec[0]/testAve[0] - newVec[1]/testAve[1] < tol and
            newVec[0]/testAve[0] - newVec[2]/testAve[2] < tol
                ):
            print(f"{testAve} is ave with {newVec[0]/testAve[0]} ava")
    else:
        if testAve[0] == 0:
            if newVec[1]/testAve[1] - newVec[2]/testAve[2] < tol and newVec[0] == 0:
                print(f"{testAve} is ave with {newVec[1]/testAve[1]} ava")
        elif testAve[1] == 0:
            if newVec[0]/testAve[0] - newVec[2]/testAve[2] < tol and newVec[1] == 0:
                print(f"{testAve} is ave with {newVec[0]/testAve[0]} ava")
        elif testAve[2] == 0:
            if newVec[0]/testAve[0] - newVec[1]/testAve[1] < tol and newVec[2] == 0:
                print(f"{testAve} is ave with {newVec[0]/testAve[0]} ava")

# Ejercicio 6
print("\nEjercicio 6:")
A = np.array([
    [1,3,2],
    [4,2,-1],
    [5,5,1]
])

eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)

# Ejercicio 8
print("\nEjercicio 8:")
A = np.array([
    [1,3,2],
    [4,2,-1],
    [5,5,1]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvectors:")
[print(eigenvector) for eigenvector in eigenvectors]

print(f"Rang of eigenvectors matrix = {np.linalg.matrix_rank(eigenvectors)}")
