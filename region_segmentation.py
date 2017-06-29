from skimage import data, io, segmentation, color
from skimage.future import graph
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
import cv2

def _weight_mean_color(graph, src, dst, n): # source: goo.gl/9kuZMH
    diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
    diff = np.linalg.norm(diff)
    return {'weight': diff}


def merge_mean_color(graph, src, dst): # source: goo.gl/9kuZMH
    graph.node[dst]['total color'] += graph.node[src]['total color']
    graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
    graph.node[dst]['mean color'] = (graph.node[dst]['total color'] /
                                     graph.node[dst]['pixel count'])

def regions2img(original_img, labels, save): 
    """ save == True: saves resulting images
        save == False: displays resulting images """
    regions = regionprops(labels+1) # if you don't add 1, one of the regions gets ignored
    num_regions = len(regions)
    # print((labels+1).shape) # <<<<<<<<<<
    # print() # <<<<<<<<<<<<<<<
    backgroung_region = -1
    imgs = []
    centroids = [] # [region_num, [centroid_x, centroid_y]]
    for i,region in enumerate(regions): 
        centroids.append([i, region['centroid'][0]])
        new_img = np.zeros((original_img.shape[0], original_img.shape[1], 4), dtype=np.uint8) 
        for pxl in region['coords']:
            if(pxl[0] == 0):
                backgroung_region = i
            original_pxl = original_img[pxl[0]][pxl[1]]
            new_img[pxl[0]][pxl[1]] = (original_pxl[0], original_pxl[1], original_pxl[2], 255)
            imgs.append(new_img)
        if save:
            io.imsave("output_images/region"+str(i)+".png", new_img)
        else:
            plt.subplot(np.ceil(num_regions/2), 2, i+1)
            plt.title('region '+str(i))
            plt.imshow(new_img)

    centroids = sorted(centroids, key=lambda x: x[1]) # <<<<<<<<<<<<<<<<
    print(centroids)
    print(backgroung_region)
    if not save:
        plt.show()

    return imgs, centroids, backgroung_region



##########################################################################################


# img = io.imread('input_images/test3.jpg')

# labels = segmentation.slic(img, compactness=30, multichannel=True, n_segments=35)
# g = graph.rag_mean_color(img, labels)
# labels2 = graph.merge_hierarchical(labels, g, thresh=52, rag_copy=False,
#                                    in_place_merge=True,
#                                    merge_func=merge_mean_color,
#                                    weight_func=_weight_mean_color)
# # g2 = graph.rag_mean_color(img, labels2)
# # out = color.label2rgb(labels2, img, kind='avg')
# # out = segmentation.mark_boundaries(img, labels2, (0, 0, 0), mode='thick')

# regions, centroids, background_region = regions2img(img, labels2, True) 


 


