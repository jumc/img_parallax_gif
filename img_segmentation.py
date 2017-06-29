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

def rearrange_regions(regions, centroids, backgroung_idx):
    sorted_centroids = sorted(centroids, key=lambda x: x[1])
    regions_order = [sorted_centroids.index(centroid) for centroid in centroids]
    bckg_old_pos = regions_order.index(backgroung_idx) # position based on centroids height
    # forces background to be the first of the list of regions:
    regions_order[bckg_old_pos], regions_order[0] = regions_order[0], regions_order[bckg_old_pos]
    return [regions[i] for i in regions_order]


def regions2img(original_img, labels, save): 
    """ save == True: saves resulting images
        save == False: displays resulting images """
    regions = regionprops(labels+1) # if you don't add 1, one of the regions gets ignored
    num_regions = len(regions)
    backgroung_idx = -1
    imgs = []
    centroids = [] # [region_num, [centroid_x, centroid_y]]
    for i,region in enumerate(regions): 
        centroids.append([i, region['centroid'][0]])
        new_img = np.zeros((original_img.shape[0], original_img.shape[1], 4), dtype=np.uint8) 
        for pxl in region['coords']:
            if(pxl[0] == 0):
                backgroung_idx = i # saves the region touching the top of the image 
            original_pxl = original_img[pxl[0]][pxl[1]]
            new_img[pxl[0]][pxl[1]] = (original_pxl[0], original_pxl[1], original_pxl[2], 255)
        imgs.append(new_img)
        if save:
            io.imsave("output_images/region"+str(i)+".png", new_img)
        else:
            plt.subplot(np.ceil(num_regions/2), 2, i+1)
            plt.title('region '+str(i))
            plt.imshow(new_img)
    if not save:
        plt.show()
    return rearrange_regions(imgs, centroids, backgroung_idx)






