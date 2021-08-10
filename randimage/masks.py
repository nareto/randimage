import numpy as np


class BaseMask(object):
    def __init__(self, shape) -> None:
        self.shape = shape


class SaltPepperMask(BaseMask):
    def get_mask(self):
        self.mask = np.random.randint(0, 2, size=self.shape)
        return self.mask


class NormalMask(BaseMask):
    def get_mask(self):
        return np.random.normal(0,1 ,size=self.shape)

class GaussianBlobMask(BaseMask):
    def get_mask(self):
        pass
