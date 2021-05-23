import sys
import argparse
import os
from PIL import Image
import fnmatch
import re 

''' a really quick "neat" function to create a subdirectory structure for media files '''

# standard_widths = [120,160,220,240,320,480,800,1024,1200]
standard_widths = ['200/','400/','600/','800/','1200/','1600/']

class ImgResizer:
    def __init__(self, path):
        self.path = path
        return 0


if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('location', type=str)
    args = parser.parse_args()

    # dirs = [dir for dir in os.listdir(args.location) if os.path.isdir(os.path.join(args.location,dir))]
    # # print(dirs)

    # # make subdirectories and structure
    # dirstomake = [[os.path.join(os.path.join(os.path.join(args.location,'../'), dir), projectDir) for dir in standard_widths] for projectDir in dirs]
    # dirstomake = [dir for dirset in dirstomake for dir in dirset]
    # [os.makedirs(dir) for dir in dirstomake]

    # use ffmpeg to scale images
    # gather all images
    imgs = [ os.path.join(dname, filename) for dname, sdname, flist in os.walk(args.location) for filename in flist if filename.endswith('.jpeg')]
    newimgs = [(img, img.replace('full sized',size[:-1])[:-5] + '_x_' + size[:-1] +  img.replace('full sized',size[:-1])[-5:],int(size[:-1])) for img in imgs for size in standard_widths]
    for (img,newimg,size) in newimgs:
        newimg = newimg.replace('.jpeg','.png')
        # print(img,newimg,size)
        image = Image.open(img)
        image.thumbnail((size,size))
        image.save(newimg,'png')