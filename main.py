import img_segmentation
import gif_maker
from skimage import data, io, segmentation, color
from skimage.future import graph
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import cv2
import imageio
import math

# imagem a ser lida
img = io.imread('input_images/test3.jpg')

print("\n- Image segmentation...", end="")

labels = segmentation.slic(img, compactness=30, multichannel=True, n_segments=35)
g = graph.rag_mean_color(img, labels)
labels2 = graph.merge_hierarchical(labels, g, thresh=52, rag_copy=False,
                                   in_place_merge=True,
                                   merge_func=img_segmentation.merge_mean_color,
                                   weight_func=img_segmentation._weight_mean_color)

regions = img_segmentation.regions2img(img, labels2, True) 

print(" Done.\n")
num_frames = 64
all_frames = []

print("\n- Gif generation...", end="")

img = gif_maker.rgb2rgba(img)
frames = gif_maker.gen_frames(0, img, num_frames, 1.0) # i = 0 is the background and doesn't need to be moved
all_frames.append(frames)

scales = [ 1, 1.5, 1.5, 2, 4, 4, 4, 4, 4] # it usually uses only 5 regions
# scales = [ 1, 2, 2, 4, 4, 4]
for i,img in enumerate(regions):
	if i != 0:
		frames = gif_maker.gen_frames(i, img, num_frames, 1 + scales[i]*0.05) 
		all_frames.append(frames)
new_frames = gif_maker.overlap_layers(all_frames)
imageio.mimsave('generated_gifs/new_gif.gif', new_frames)

print(" Done.\n")

