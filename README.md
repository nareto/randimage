## IDEA 1
+ 1 generate random grayvalue n x n mask
+ 2 pick random starting point
+ 3 create region-filling path by using cellular-automata-like rule based on mask 
+ 4 pick random matplotlib colormap and color path from first to last point using full range of colormap


## IDEA 2:
+ 1 generate random gaussian blobs in a n x n grayvalue mask
+ 2 define regions on the mask from level sets (in and out regions)
+ 3 use RBEPWT region filling path on all regions
+ 4 color paths using random matplotlib colormap


