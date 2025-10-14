import numpy as np

def z(W, b, x):
    return W @ x + b

def sigm(z):
    return 1/(1 + np.exp(-z))

def dsigm_dz(z):
    return np.exp(-z)/(1 + np.exp(-z))**2

def J(y_hat, y):
    return 0.5 * (y_hat - y)**2

w1 = np.array([
    [ 0.1, -0.5 ],
    [-0.3, -0.9 ],
    [ 0.8,  0.02]
])
b1 = np.array([
    [0.1],
    [0.5],
    [0.8]
])

w2 = np.array([
    [ -0.4, 0.2, -0.5],
])
b2 = 0.7

x = np.array([
    [ 1.8],
    [-3.4]
])
y = 5

z1 = z(w1, b1, x)
print(f"z1 = {z1}")
f1 = sigm(z1)
print(f"f1 = {f1}")
z2 = z(w2, b2, f1)
print(f"z2 = {z2}")
f2 = sigm(z2)
print(f"f2 = {f2}")
j = J(f2, y)
print(f"J = {j}")

dJ_df2 = f2 - y
df2_dz2 = dsigm_dz(z2)
dJ_db2 = dJ_df2 * df2_dz2
print(f"dJ_db2 = {dJ_db2}")
dJ_dw2 = dJ_df2 * df2_dz2 * f1.transpose()
print(f"dJ_dw2 = {dJ_dw2}")
print(f"dJ_df2 = {dJ_df2}")
print(f"df2_dz2 = {df2_dz2}")
dz2_df1 = w2
print(f"dz2_df1 = {dz2_df1}")
print(f"{dsigm_dz(z1)}")
df1_dz1 = np.diag(dsigm_dz(z1).flatten())
print(f"df1_dz1 = {df1_dz1}")
dz1_dw1 = x
print(dz2_df1.shape)
print(df1_dz1.shape)
print(dz1_dw1.shape)
# dJ_dw1 = dJ_df2 @ df2_dz2 @ dz2_df1.transpose() @ df1_dz1.transpose() @ dz1_dw1.transpose()
# print(df2_dz2 * dJ_df2)
# print(dz2_df1)
print(f"{df1_dz1.shape} x {dz2_df1.shape}")
# print(df1_dz1 @ dz2_df1)
print(dz2_df1 @ df1_dz1)
# print(dz2_df1.transpose() @ df2_dz2.transpose())
# print((df1_dz1 @ (dz2_df1 * (df2_dz2 @ dJ_df2))))
# dJ_dw1 = dz1_dw1 @ np.array([(df1_dz1 @ (dz2_df1 * (df2_dz2 * dJ_df2)))])
dJ_dw1 = dJ_df2 * df2_dz2 * (dz2_df1 @ df1_dz1).transpose() @ dz1_dw1.transpose()
print(f"dJ_d21 = {dJ_dw1}")

