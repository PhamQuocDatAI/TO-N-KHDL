# Tính A^n:
import numpy as np
import random


def matrix(m, n):
    matrix = np.random.randint(-10, 10, size = (m, n))
    return matrix

print(matrix(3, 4))