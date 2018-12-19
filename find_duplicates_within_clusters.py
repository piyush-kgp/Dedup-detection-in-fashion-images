import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import time
import skimage
import KMeans
import itertools
from collections import defaultdict
import json

img_dir = 'Images'
img_files = os.listdir(img_dir)
img_files = sorted(img_files)

def duplicated(img1, img2, thresh = 0.9):
    """
    Measures duplication using SSIM metric (because that is what we used in clustering)
    We should use the same distance function in clustering step and finding duplication
    step. Returns a Boolean of whether or not img1 and img2 are same (Default Threshold 0.9)
    """
    return skimage.measure.compare_ssim(img1, img2, multichannel = True) > thresh

#images_in_clusters is a dict of all images in a cluster
_, clusters = KMeans.KMeans('Images/').k_means_clustering()
images_in_clusters = defaultdict(list)

for i, img_file in enumerate(img_files):
    images_in_clusters[clusters[i]].append(img_file)

duplicates = {}
total_duplicates = []
for clust in set(clusters):
    images_in_cluster = images_in_clusters[clust]
    for comb in itertools.combinations(images_in_cluster, 2):
        duplicates[comb] = duplicated(comb)
    #Filter out the Falses
    duplicates_found = {k: v for k, v in duplicates.items() if v}
    total_duplicates.append(duplicates_found)

with open('duplicates_within_clusters.json', 'w') as outfile:
    json.dump(total_duplicates, outfile)
