import random
import matplotlib.pyplot as plt
import numpy as np
from .masks import MASKS
from .paths import PATHS
from .coloredpath import ColoredPath

def show_array(array, cmap='gray'):
    plt.imshow(array, cmap=cmap)
    plt.tight_layout()
    plt.axis('off')
    plt.show()


def show_img_list(img_list, shape, cmap='gray', figsize=None):
    # figs, axis = plt.subplots(shape[0],shape[1])
    nrow,ncol = shape
    if figsize is None: figsize = (ncol + 1, nrow + 1)
    fig, axis = plt.subplots(
        nrow, ncol,
        gridspec_kw=dict(wspace=0.0, hspace=0.0,
                         top=1. - 0.5 / (figsize[1]), bottom=0.5 / (figsize[1]),
                         left=0.5 / (figsize[0]), right=1 - 0.5 / (figsize[0])),
        figsize=figsize,
        sharey='row', sharex='col',  # optionally
    )
    for idx, img in enumerate(img_list):
        row, col = np.unravel_index(idx, shape=shape)
        ax = axis[row, col]
        ax.imshow(img, cmap=cmap)
        ax.axis('off')
    fig.show()
    return fig

def get_random_image(img_size):
    mask = random.choice(MASKS)(img_size).get_mask()
    path = random.choice(PATHS)(mask).get_path()
    img = ColoredPath(path, img_size).get_colored_path()
    return img