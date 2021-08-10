import matplotlib.pyplot as plt
import numpy as np


def show_array(array, cmap='gray'):
    plt.imshow(array, cmap=cmap)
    plt.axis('off')
    plt.show()


def show_img_list(img_list, shape, cmap='gray'):
    # figs, axis = plt.subplots(shape[0],shape[1])
    nrow,ncol = shape
    fig, axis = plt.subplots(
        nrow, ncol,
        gridspec_kw=dict(wspace=0.0, hspace=0.0,
                         top=1. - 0.5 / (nrow + 1), bottom=0.5 / (nrow + 1),
                         left=0.5 / (ncol + 1), right=1 - 0.5 / (ncol + 1)),
        figsize=(ncol + 1, nrow + 1),
        sharey='row', sharex='col',  # optionally
    )
    for idx, img in enumerate(img_list):
        row, col = np.unravel_index(idx, shape=shape)
        ax = axis[row, col]
        ax.imshow(img, cmap=cmap)
        ax.axis('off')
    # plt.tight_layout()
    plt.show()
