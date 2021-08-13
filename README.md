# randimage - create random images in python
![randimage example](randimage.png)

This package comes out of frustration: I could not find a simple way to generate random profile pictures for users of my app [riffandmatch](https://riffandmatch.com).

Now it's as simple as

    from randimage import get_random_image, show_array
    img_size = (128,128)
    img = get_random_image(img_size)  #returns numpy array
    show_array(img) #shows the image

To save the image you can use `matplotlib`:

    import matplotlib
    matplotlib.image.imsave("randimage.png", img)

In `examples.py` you can find slightly more detailed code showing for example how to manually choose and combine the masks and path finding procedures.

## Installation

    pip install randimage

## How it works
You can read [this post](https://renatobudinich.com/create-random-images-with-randimage) on my blog for a full explanation of how the procedure works.

The basic idea is to generate a random region-filling path for the image, then pick a colormap from `matplotlib` and use it to progressively color the pixels in the image as ordered by the path.

To generate the path we start from a random gray-valued mask (of which you can find several examples in `masks.py`) of the same size of the final image and apply to it either the EPWT (Easy Path Wavelet Transform) **[1]** path-finding procedure or a novel probabilistic path finding.

In both cases the starting point is chosen randomly and for each point a neigborhood is considered, which does not include points that are already part of the path. For the EPWT, each subsequent point in the path is chosen in this neighborhood as the one whose gray value is closest in absolute value to the current point. For the probabilistic path instead, a random point in the neighborhood is chosen using the gray values as probability weights.

In the future I would like to try and use the path finding procedure of the RBEPWT (Region Based Easy Path Wavelet Transform) **[2]** and experiment with rule-based [cellular automata](https://en.wikipedia.org/wiki/Cellular_automaton) to construct paths with greater self-similarity.


**[1]** Gerlind Plonka. **The easy path wavelet transform: A new adaptive wavelet transform for sparse representation of two-dimensional data.** *Multiscale
Modeling & Simulation*, 7(3):1474–1496, 2008.

**[2]** Budinich, R. (2017). **A region-based easy-path wavelet transform for sparse image representation.** *International Journal of Wavelets, Multiresolution and Information Processing,* 15(05), 1750045.