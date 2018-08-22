#!/usr/bin/env python

import argparse
import imageio
import numpy as np

# Create parser
parser = argparse.ArgumentParser()
parser.add_argument('--image1', type=str)
parser.add_argument('--image2', type=str)
parser.add_argument('--output', type=str)
args = parser.parse_args()

# Read images
image1 = np.array(imageio.imread(args.image1), dtype='int64')
image2 = np.array(imageio.imread(args.image2), dtype='int64')

# Ensure both images have the same dimensions
assert image1.shape == image2.shape

# Combine images
image_combined = np.array(np.divide(image1 + image2, 2), dtype='uint8')

# Save image
imageio.imwrite(args.output, image_combined)
