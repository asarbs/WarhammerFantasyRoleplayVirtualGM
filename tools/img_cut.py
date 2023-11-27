#!/usr/bin/env python3.11

import os
import glob
import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000

img = PIL.Image.open(os.path.join("WarhammerFantasyRoleplayVirtualGM_site", "WarhammerFantasyRoleplayVirtualGM_map", "static", "img", "SHDMotWOW.jpg"))
img.show()
org_size = img.size

size = 256 * 5

rm_path = os.path.join("WarhammerFantasyRoleplayVirtualGM_site", "WarhammerFantasyRoleplayVirtualGM_map", "static", "img")
jpgFilenamesList = glob.glob( rm_path + '/SHDMotWOW_*.jpg')
for f in jpgFilenamesList:
    os.remove(f)

for x in range(0, org_size[0], size):
    for y in range(0, org_size[1], size):
        box = (x, y, x + size, y + size)
        img2 = img.crop(box)
        path = os.path.join("WarhammerFantasyRoleplayVirtualGM_site", "WarhammerFantasyRoleplayVirtualGM_map", "static", "img", "SHDMotWOW_{}_{}.jpg".format( int(x / size), int(y / size)))
        print(path)
        img2.save(path)
