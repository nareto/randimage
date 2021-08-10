import matplotlib.pyplot as plt

def show_array(array, cmap='gray'):
    plt.imshow(array, cmap=cmap)
    plt.axis('off')
    plt.show()