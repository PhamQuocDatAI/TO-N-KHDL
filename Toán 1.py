# Viết 1 hàm tạo ra 1 ma trận số nguyên có định thức bằng 1.
import numpy as np
import ranndom


def det_one(low: int, high: int, a: int):
    det_one = np.random.randint(low, high, size = (a, a))
    while np.linalg.det(det_one) != 1:
        det_one = np.random.randint(low, high, size = (a, a))
    return det_one