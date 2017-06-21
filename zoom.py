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

def create_frames(layers, nlayers, nframes, height, width):
# Horizontal scroll
    frames = []
    z_height, z_width = layers[0].shape[:2]
    cuts = []
    alpha =  np.linspace(0.01, 0.5, nlayers) # 1 >= alpha > 0 : speed of movement
    for i in range(nlayers):
        cuts.append(np.linspace(0, (z_width - width)*alpha[i], nframes, dtype=int))
    for i in range(nframes):
        j = 0
        curr_frame = layers[0]
        for j in range(nlayers):
            # Change(deslocate) cut values based on current frame index and layer number        
            cut_w = int((z_width - width)/2)
            cut_h = int((z_height - height)/2)

            if((cuts[j][i] - cut_w) >= 0):
                beta = cuts[j][i]
            else:
                beta = cut_w
            layer_frame = layers[j][cut_h:(-cut_h), cut_w - beta:-(cut_w + beta)]
            # Merge acquired layer_frame and append to frames
            curr_frame = cv2.add(curr_frame, layers[j])
            # cv2.addWeighted(curr_frame, 0.5, layers[j], 0.5, 0, curr_frame) # Problem: counting alpha as black
            
        frames.append(curr_frame)
        cv2.imshow(str(i),curr_frame)
        cv2.waitKey(0)
        cv2.imwrite("output_frames/frame"+str(i)+".png", curr_frame)

    return frames

def gif(imgs):
#http://www.nooganeer.com/his/projects/image-processing/making-a-gif-with-opencv-and-scikit-image-in-python/
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
 
    ims = map(lambda x: (ax.imshow(x), ax.set_title('')), imgs)
    im_ani = animation.ArtistAnimation(fig, ims, interval=800, repeat_delay=0, blit=False)
    # plt.show()
    im_ani.save('parallax.gif',writer="imagemagick")

scale = 1.05
nframes = 24
nlayers = 5
layers = []

for i in range(nlayers):
    layer = cv2.imread("output_images/region"+str(i)+".png", -1)
    layers.append(zoom(layer, scale))
height, width = layer.shape[:2]
gif(create_frames(layers, nlayers, nframes, height, width))