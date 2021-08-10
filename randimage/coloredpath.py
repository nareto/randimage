import numpy as np
import matplotlib.pyplot as plt

class ColoredPath:
    def __init__(self, path, shape) -> None:
        self.path = path
        self.img = np.zeros((shape[0],shape[1],3))

    def get_colored_path(self, cmap='viridis'):
        mpl_cmap = plt.cm.get_cmap(cmap)
        path_length = len(self.path)
        for idx,point in enumerate(self.path):
            self.img[point] = mpl_cmap(idx/path_length)[:3]
        return self.img


