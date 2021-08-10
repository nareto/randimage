# %% 
## GENERATE SOME RANDOM IMAGES
from randimage import get_random_image, show_img_list

%reload_ext autoreload
%autoreload 2


SHAPE = (5, 8)
SIZE = SHAPE[0]*SHAPE[1]
imgs = []
img_size = ((64,64))
for i in range(SIZE):
    img = get_random_image(img_size)
    imgs.append(img)
show_img_list(imgs, SHAPE)

#%%
# MANUALLY DEFINE MASK AND PATH MODULES
from randimage import GaussianBlobMask, NormalMask, SaltPepperMask, EPWTPath, ColoredPath, show_array

mask = SaltPepperMask(img_size).get_mask()
# mask = NormalMask(img_size).get_mask()
# mask = GaussianBlobMask(img_size).get_mask(5)

# show_array(mask, cmap='gray')

# mask = GaussianBlobMask().get_mask()

path = EPWTPath(mask).get_path()

img = ColoredPath(path, mask.shape).get_colored_path()

show_array(img)

#%%
# SAVE THE IMAGE
import matplotlib
matplotlib.image.imsave("randimage.png", img)

