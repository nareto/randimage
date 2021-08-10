from randimage import GaussianBlobMask, EPWTPath, ColoredPath

mask = GaussianBlobMask().get_mask()
path = EPWTPath(mask).get_path()
colored_path = ColoredPath(path)