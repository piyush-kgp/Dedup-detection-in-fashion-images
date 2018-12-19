import cv2
import os
import numpy as np
import time
import skimage
import KMeans
import itertools
from collections import defaultdict
import json
from skimage.measure import compare_ssim

img_dir = '../Images'
img_files = os.listdir(img_dir)
img_files = sorted(img_files)

def ssim_similarity(img1, img2):
    """
    Measures duplication using SSIM metric (because that is what we used in clustering)
    We should use the same distance function in clustering step and finding duplication
    step. Returns a Boolean of whether or not img1 and img2 are same (Default Threshold 0.9)
    """
    return compare_ssim(img1, img2, multichannel = True)


def duplicated(img_file1, img_file2, thresh = 0.9):
    """
    Measures duplication using SSIM metric (because that is what we used in clustering)
    We should use the same distance function in clustering step and finding duplication
    step. Returns a Boolean of whether or not img1 and img2 are same (Default Threshold 0.9)
    """
    img1 = cv2.resize(cv2.imread(img_file1), (299, 299))
    img2 = cv2.resize(cv2.imread(img_file2), (299, 299))
    return skimage.measure.compare_ssim(img1, img2, multichannel = True) > thresh

#Although we dont really care about the centroids
centroids, clusters = KMeans.KMeans(img_dir = '../Images/', distance_function = ssim_similarity).k_means_clustering()
#images_in_clusters is a dict of all images in a cluster
images_in_clusters = defaultdict(list)

# for i, img_file in enumerate(img_files):
#     images_in_clusters[clusters[i]].append(img_file)

for i, img_file in enumerate(img_files):
    if i<10:
        images_in_clusters[clusters[i]].append(img_file)
    else:
        pass

duplicates = {}
total_duplicates = defaultdict(list)
for clust in list(set(clusters)):
    images_in_cluster = images_in_clusters[clust]
    for comb in itertools.combinations(images_in_cluster, 2):
        file1, file2 = os.path.join(img_dir, comb[0]), os.path.join(img_dir, comb[1])
        if duplicated(file1, file2):
            total_duplicates[file1[10:-4].upper()].append(file2[10:-4].upper())

with open('duplicates_within_clusters.json', 'w') as outfile:
    json.dump(total_duplicates, outfile)
