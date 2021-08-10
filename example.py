# %%
from randimage.utils import show_img_list
from randimage import GaussianBlobMask, SaltPepperMask, NormalMask, EPWTPath, ColoredPath, show_array
%reload_ext autoreload
%autoreload 2



SHAPE = (5, 8)
SIZE = SHAPE[0]*SHAPE[1]
masks = []
imgs = []
img_size = ((64,64))
for i in range(SIZE):
    # mask = SaltPepperMask(img_size).get_mask()
    mask = NormalMask(img_size).get_mask()
    # mask = GaussianBlobMask(img_size).get_mask(5)
    masks.append(mask)
    # show_array(mask, cmap='gray')

    # mask = GaussianBlobMask().get_mask()
    path = EPWTPath(mask).get_path()
    img = ColoredPath(path, mask.shape).get_colored_path()
    imgs.append(img)
#%%
show_img_list(imgs, SHAPE)
# print(path)
# %%
show_array(masks[1])