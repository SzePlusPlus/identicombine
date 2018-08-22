#!/usr/bin/env python

import argparse
import imageio
import numpy as np

# Create parser
parser = argparse.ArgumentParser()
parser.add_argument('--image1', type=str)
parser.add_argument('--image2', type=str)
parser.add_argument('--output', type=str)
parser.add_argument('--algo', type=str, default='average')
args = parser.parse_args()

# Read images
image1 = np.array(imageio.imread(args.image1), dtype='int64')
image2 = np.array(imageio.imread(args.image2), dtype='int64')

# Ensure both images have the same dimensions
assert image1.shape == image2.shape

# Combine images
if args.algo == 'average':
	image_combined = np.divide(image1 + image2, 2)
elif args.algo == 'overlay':
	gray = np.array([240, 240, 240])
	image_combined = np.where(image2 == gray, image1, image2)

# Save image
imageio.imwrite(args.output, np.array(image_combined, dtype='uint8'))
