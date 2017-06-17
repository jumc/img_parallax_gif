"""
===========
RAG Merging
===========

This example constructs a Region Adjacency Graph (RAG) and progressively merges
regions that are similar in color. Merging two adjacent regions produces
a new region with all the pixels from the merged regions. Regions are merged
until no highly similar region pairs remain.

"""

from skimage import data, io, segmentation, color
from skimage.future import graph
import numpy as np
from skimage.transform import rescale, resize, downscale_local_mean
import matplotlib.pyplot as plt


def _weight_mean_color(graph, src, dst, n):
    """Callback to handle merging nodes by recomputing mean color.

    The method expects that the mean color of `dst` is already computed.

    Parameters
    ----------
    graph : RAG
        The graph under consideration.
    src, dst : int
        The vertices in `graph` to be merged.
    n : int
        A neighbor of `src` or `dst` or both.

    Returns
    -------
    data : dict
        A dictionary with the `"weight"` attribute set as the absolute
        difference of the mean color between node `dst` and `n`.
    """

    diff = graph.node[dst]['mean color'] - graph.node[n]['mean color']
    diff = np.linalg.norm(diff)
    return {'weight': diff}


def merge_mean_color(graph, src, dst):
    """Callback called before merging two nodes of a mean color distance graph.

    This method computes the mean color of `dst`.

    Parameters
    ----------
    graph : RAG
        The graph under consideration.
    src, dst : int
        The vertices in `graph` to be merged.
    """
    graph.node[dst]['total color'] += graph.node[src]['total color']
    graph.node[dst]['pixel count'] += graph.node[src]['pixel count']
    graph.node[dst]['mean color'] = (graph.node[dst]['total color'] /
                                     graph.node[dst]['pixel count'])


img = io.imread('test3.jpg')
# print(img.shape)
# img = resize(img, (800,1200, 3), mode='reflect')
print(img.shape)
# img = downscale_local_mean(img,(6,6,1))
# img = rescale(img, 0.2)
# img = data.coins()
# plt.subplot(5, 6, 1)
# plt.title("original")
# plt.imshow(img)

for i in range(6):
    for j in range(1, 6):
        labels = segmentation.slic(img, compactness=30, multichannel=True, n_segments=(35+i*18))
        g = graph.rag_mean_color(img, labels)

        labels2 = graph.merge_hierarchical(labels, g, thresh=31+7*j, rag_copy=False,
                                           in_place_merge=True,
                                           merge_func=merge_mean_color,
                                           weight_func=_weight_mean_color)

        g2 = graph.rag_mean_color(img, labels2)

        out = color.label2rgb(labels2, img, kind='avg')
        out = segmentation.mark_boundaries(out, labels2, (0, 0, 0))
        # io.imshow(out)
        # io.show()
        plt.subplot(6, 5, 5*i+j) 
        plt.title(str(35+i*18)+'/'+str(31+7*j))
        plt.imshow(out)
        print("#",str(i)," done")

import winsound
winsound.Beep(1000,700) # lembrar de desabilitar o som do windows de novo

plt.show()
# melhor até agora = 35/52 multichannel=True