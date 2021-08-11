# %% 
## GENERATE SOME RANDOM IMAGES
from randimage import get_random_image, show_img_list

# %reload_ext autoreload
# %autoreload 2

#%%
SHAPE = (2, 8)
SIZE = SHAPE[0]*SHAPE[1]
imgs = []
img_size = (64,64)
for i in range(SIZE):
    img = get_random_image(img_size)
    imgs.append(img)
figure = show_img_list(imgs, SHAPE)
#%%
# SAVE THE FIGURE
figure.savefig('test1.png')
#%%
# MANUALLY DEFINE MASK AND PATH MODULES
from randimage import GaussianBlobMask, NormalMask, SaltPepperMask, EPWTPath, ProbabilisticPath, ColoredPath, show_array

img_size = (64,64)
# mask = SaltPepperMask(img_size).get_mask()
# mask = NormalMask(img_size).get_mask()
mask = GaussianBlobMask(img_size).get_mask(5)

# show_array(mask, cmap='gray')

# mask = GaussianBlobMask().get_mask()

epwtpath = EPWTPath(mask).get_path()
ppath = ProbabilisticPath(mask).get_path()

cmap = 'Spectral'
epwtimg = ColoredPath(epwtpath, mask.shape).get_colored_path(cmap)
pimg = ColoredPath(ppath, mask.shape).get_colored_path(cmap)

show_array(epwtimg)
show_array(pimg)

#%%
# SAVE THE IMAGE
import matplotlib
matplotlib.image.imsave("randimage1.png", img)

