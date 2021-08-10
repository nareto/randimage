#%%
%reload_ext autoreload
%autoreload 2
from randimage import GaussianBlobMask, SaltPepperMask, NormalMask, EPWTPath, ColoredPath, show_array

# mask = SaltPepperMask((100,100)).get_mask()
mask = NormalMask((100,100)).get_mask()
# mask = GaussianBlobMask().get_mask()
path = EPWTPath(mask).get_path()
colored_path = ColoredPath(path, mask.shape).get_colored_path('hsv')

show_array(colored_path)
# print(path)
# %%
