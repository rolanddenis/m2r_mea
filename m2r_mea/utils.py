__all__ = [
    'gen_sorted_rand',
]

import numpy as np

def gen_sorted_rand(length):
    return np.sort(np.random.rand(length))
