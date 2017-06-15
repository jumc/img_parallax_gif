import cv2
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation

def zoom(original, scale):
	height, width = original.shape[:2]

	new_w = np.ceil(width*scale).astype(int)
	new_h = np.ceil(height*scale).astype(int)

	zoomed = cv2.resize(original, (new_w, new_h), interpolation=cv2.INTER_CUBIC)

	return zoomed

def create_frames(layers, nframes, height, width):
# TO DO: Move and merge layers	
	frames = []
	z_height, z_width = layers[0].shape[:2]

	for i in xrange(nframes):
		# Iterate over layers
		# Change(deslocate) cut values based on current frame index and layer number
		cut_w = ((z_width - width)/2).astype(int)
		cut_h = ((z_height - height)/2).astype(int)
		layer_frame = layer1[cut_h:-cut_h, cut_w:-cut_w]
		# Merge acquired layer_frame and append to frames

	return frames

def gif(imgs):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
 
    ims = map(lambda x: (ax.imshow(x), ax.set_title('')), imgs)
    im_ani = animation.ArtistAnimation(fig, ims, interval=800, repeat_delay=0, blit=False)
    
    im_ani.save('parallax.gif')
    plt.show()


scale = 1.05
nframes = 24
layers = []

layer1 = cv2.imread("img/layer1.png", -1)
layers.append([zoom(layer1, scale)])
layer2 = cv2.imread("img/layer2.png", -1)
layers.append([zoom(layer2, scale)])
layer3 = cv2.imread("img/layer3.png", -1)
layers.append([zoom(layer3, scale)])
layer4 = cv2.imread("img/layer4.png", -1)
layers.append([zoom(layer4, scale)])


height, width = layer1.shape[:2]
gif(create_frames(layers, nframes, height, width))