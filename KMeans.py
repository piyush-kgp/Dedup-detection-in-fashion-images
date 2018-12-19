import cv2
import os
import numpy as np
import time
import skimage
# from skimage.measure import structural_similarity as ssim

img_dir = 'Images'
img_files = os.listdir(img_dir)
img_files = sorted(img_files)

def dist_measure(img1, img2):
    """
    Here we have demonstrated with SSIM. This can also be done with Hamming distance
    or Hellinger/Bhattacharya distance. Our KMeans class can take any distance function
    as its argument
    """
    return skimage.measure.compare_ssim(img1, img2, multichannel = True)

class KMeans:
    """
    K-means clustering of images in a directory with Custom distance.
    Borrows some functions from Scikit-Learn implementation of the algorithm
    """
    def __init__(self, img_dir, K=100, distance_function = dist_measure):
        self.distance_function = distance_function
        self.K = K
        img_files = os.listdir(img_dir)
        img_files = sorted(img_files)
        img_stack = np.zeros((len(img_files), 299, 299, 3))
        for i, img_file in enumerate(img_files):
            img = cv2.imread(os.path.join(img_dir, img_file))
            img_stack[i] = cv2.resize(img, (299, 299))
        self.data = img_stack

    def get_initial_centroids(self, seed=1):
        """"
        Randomly choose k data points as initial centroids
        Args: data - A dataset of shape N, D
        """
        n = self.data.shape[0]
        np.random.seed(seed)
        rand_indices = np.random.randint(0, n, K)
        self.centroids = self.data[rand_indices]
        return self.centroids

    def centroid_pairwise_dist(self):
        """
        Calculates a NxK distance matrix between each data point to each centroid
        This matrix needs to be evaluated at each iteration of the K-Means algorithm
        """
        distance_matrix = []
        for i, data_point in enumerate(self.data):
            distance_matrix[i] = np.array([self.distance_function(data_point, centroid) for centroid in self.centroids])
        return distance_matrix

    def assign_clusters(self):
        """
        Assignes new clusters using distances from the current centroids
        """
        distances_from_centroids = self.centroid_pairwise_dist()
        cluster_assignment = np.argmin(distances_from_centroids,axis=1)
        return cluster_assignment

    def revise_centroids(self):
        """
        Calculates new centroids with the current assigned clusters
        """
        cluster_assignment = self.assign_clusters()
        new_centroids = []
        for i in range(self.K):
            member_data_points = self.data[cluster_assignment==i]
            centroid = member_data_points.mean(axis=0)
            new_centroids.append(centroid)
        new_centroids = np.array(new_centroids)
        return new_centroids

    def k_means_clustering(self, maxiter = 100):
        """
        Performs K-Means Clustering by iterating the steps of cluster assignment and centroid revision
        """
        centroids = self.get_initial_centroids()
        prev_cluster_assignment = None
        for itr in range(maxiter):
            cluster_assignment = self.assign_clusters()
            centroids = self.revise_centroids()
            if prev_cluster_assignment is not None and (prev_cluster_assignment==cluster_assignment).all():
                #convergence check
                break
            if prev_cluster_assignment is not None:
                prev_cluster_assignment = cluster_assignment
        return self.centroids, self.cluster_assignment
