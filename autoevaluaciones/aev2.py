import numpy as np

# Ejercicio 2
exSet = [ np.array([1,2,1]), np.array([3,0,-1]), np.array([-1,2,-3]) ]
newSet = []

for vec in exSet:
    k = vec     
    for ki in newSet:
        k = k - ki * (vec @ ki) / (ki @ ki)
    k = k / np.linalg.norm(k)
    newSet.append(k)

print(f"ki = {newSet}")


