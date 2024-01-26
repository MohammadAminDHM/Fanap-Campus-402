import numpy as np
from .random_number import generate

def array_generator(count):
    """Generate an array of count elements with random numbers."""
    return np.array([generate() for _ in range(count)])
