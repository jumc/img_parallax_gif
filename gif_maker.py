import imageio
import cv2
import numpy as np
import matplotlib.pyplot as plt 
from skimage import data, io, segmentation, color
from skimage.future import graph
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import math

def zoom(original, scale):
    height, width = original.shape[:2]

    new_w = np.ceil(width*scale).astype(int)
    new_h = np.ceil(height*scale).astype(int)

    zoomed = cv2.resize(original, (new_w, new_h), interpolation=cv2.INTER_CUBIC)
    return zoomed

def gen_frames(layer_idx, original, num_frames, scale):
	zoomed = zoom(original, scale)
	delta_h = zoomed.shape[0] - original.shape[0] # vertical excess created after zoom
	delta_w = zoomed.shape[1] - original.shape[1] # horizontal excess created after zoom
	w_step = math.floor(delta_w/num_frames)
	frames = []
	row0 = math.floor(delta_h/2)
	for i in range(num_frames):
		col0 = i * w_step
		new_frame = zoomed[delta_h : original.shape[0] + delta_h, col0 : col0 + original.shape[1]-15]
		frames.append(new_frame)

	return frames


def overlap_layers(all_frames):
	new_frames = []
	for i in range(24):
		new_frame = np.zeros(all_frames[0][0].shape, dtype=np.uint8) 
		for row in range(new_frame.shape[0]):
			for col in range(new_frame.shape[1]):
				for layer in range(len(all_frames)):
					if(new_frame[row][col][3]!=255):
						new_frame[row][col] = all_frames[4-layer][i][row][col] #<<<<
		new_frames.append(new_frame)
	return new_frames

def rgb2rgba(original):
	new_image = np.zeros((original.shape[0],original.shape[1], 4), dtype=np.uint8)
	for row in range(original.shape[0]):
		for col in range(original.shape[1]):
			original_pxl = original[row][col]
			new_image[row][col] = (original_pxl[0], original_pxl[1], original_pxl[2], 255)
	return new_image




