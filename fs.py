#! /usr/bin/python3

import numpy as np
import glob
from skimage import io, filters

folder = "pcb"
image_filenames = sorted(glob.glob(folder+"/pcb_*"))

# load color images
images = [io.imread(img) for img in image_filenames]

# load gray scale images
gray_images = [filters.laplace(io.imread(img, as_gray = True)) for img in image_filenames ]

# initialize stack
focus_stack = np.zeros_like(images[0])

focus_measure = np.zeros_like(gray_images[0])

for i, gray_image in enumerate(gray_images):
    focus_measure = np.maximum(focus_measure, gray_image)
    print(np.sum(np.abs(gray_image)))
    focus_stack[focus_measure == gray_image] = images[i][focus_measure == gray_image]

io.imsave('focus_stacked_image.jpg', focus_stack)
