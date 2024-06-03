from typing import Tuple
import numpy as np


def random_uniform_union(from1: float, to1: float, from2: float, to2: float):
    if np.random.rand() < 0.5:
        # Generate a random float in the range [from1, to1)
        return np.random.uniform(from1, to1)
    else:
        # Generate a random float in the range [from2+1, 5=to2)
        return np.random.uniform(from2, to2)
