import numpy as np


def generate_rgb_noise(dim: tuple) -> np.ndarray:
    return (np.random.random(dim) * 256).astype(np.uint8)

