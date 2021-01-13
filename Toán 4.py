import numpy as np
import random


A = np.random.randint(10, size=(3, 4))
print(A)

# Phân tích SVD 
U, S, V = np.linalg.svd(A)
print(U)
print("-"*50)
print(S)
print("-"*50)
print(V)
UT = np.transpose(U)
print(U@UT)
print("-"*50)
sigma = np.zeros((3, 4))
for i, x in enumerate(S):
    sigma[i, i] = x  
print(sigma)
print("-"*50)
B = U@sigma@V
print(B)
print("-"*50)
print(A - B)