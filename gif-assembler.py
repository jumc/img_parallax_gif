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

def gif(imgs):
    # http://www.nooganeer.com/his/projects/image-processing/making-a-gif-with-opencv-and-scikit-image-in-python/
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
 
    ims = map(lambda x: (ax.imshow(x), ax.set_title('')), imgs)
    im_ani = animation.ArtistAnimation(fig, ims, interval=800, repeat_delay=0, blit=False)
    # plt.show()
    im_ani.save('parallax.gif',writer="imagemagick")

layers = []
frames = []
nlayers = 5
nframes = 24
t = 1/100
scale = 1.05

layer = cv2.imread("output_images/region0.png", -1)

# Get layers zoomed in
for i in range(nlayers):
    layer = cv2.imread("output_images/region"+str(i)+".png", -1)  
    layers.append(zoom(layer, scale))

# Set variable for cut and assembly
h, w = layers[0].shape[:2]
shift = np.ceil(np.linspace(1, w*scale*t, nlayers)).astype(int)
cut_x = np.zeros(nlayers, dtype=int)
gif_redux = shift[-1]*nframes

# For each frame assemble correct images with correct cut
for frame in range(nframes):
    img = np.zeros((h, w - gif_redux, 4), dtype=np.uint8)

    for i in range(nlayers):
        cut_w = w - gif_redux + cut_x[i]

        cut_img = layers[i][0:h, cut_x[i]:cut_w]
        img = cv2.add(img, cut_img)

        # After each frame each layer makes a shift
        cut_x[i] += shift[i]

    frames.append(img)
    # cv2.imshow("Frame #"+str(i), img)
    # cv2.waitKey(0)
    
i = 0
for frame in frames:
    cv2.imwrite("frames/frame"+str(i)+".png", frame)
    i += 1
