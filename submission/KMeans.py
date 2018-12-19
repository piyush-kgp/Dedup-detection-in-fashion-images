import cv2
import os
import numpy as np
import time
import skimage

class KMeans:
    """
    K-means clustering of images in a directory with Custom distance.
    Borrows some functions from Scikit-Learn implementation of the algorithm.
    Be reminded that this will take time due to large size of data
    """
    def __init__(self, img_dir,distance_function, K=100, maxiter = 3, optimize = np.argmin):
        self.optimize = optimize
        self.distance_function = distance_function
        self.K = K
        self.maxiter = maxiter
        img_files = os.listdir(img_dir)
        img_files = sorted(img_files)
        # img_stack = np.zeros((len(img_files), 299, 299, 3))
        img_stack = np.zeros((10, 299, 299, 3))
        # for i, img_file in enumerate(img_files):
        #     img = cv2.imread(os.path.join(img_dir, img_file))
        #     img_stack[i] = cv2.resize(img, (299, 299))
        for i, img_file in enumerate(img_files):
            if i<10:
                print(i)
                img = cv2.imread(os.path.join(img_dir, img_file))
                img_stack[i] = cv2.resize(img, (299, 299))
            else:
                pass
        self.data = img_stack

    def get_initial_centroids(self, seed=1):
        """"
        Randomly choose k data points as initial centroids
        Args: data - A dataset of shape N, D
        """
        n = self.data.shape[0]
        np.random.seed(seed)
        rand_indices = np.random.randint(0, n, self.K)
        self.centroids = self.data[rand_indices]
        return self.centroids

    def centroid_pairwise_dist(self):
        """
        Calculates a NxK distance matrix between each data point to each centroid
        This matrix needs to be evaluated at each iteration of the K-Means algorithm
        """
        distance_matrix = np.zeros((self.data.shape[0], self.K))
        for i, data_point in enumerate(self.data):
            distance_matrix[i] = np.array([self.distance_function(data_point, centroid) for centroid in self.centroids])
        # print(distance_matrix)
        return distance_matrix

    def assign_clusters(self):
        """
        Assignes new clusters using distances from the current centroids. The important thing to note is that
        unlike traditional clustering where the distance metric is used to assign centroids, if we use a similarity
        metric then we have to assign each point to a centroid with the maximum similarity rather than the minimum distance.
        (and hence np.argmax rather than the traditional np.argmin)
        """
        distances_from_centroids = self.centroid_pairwise_dist()
        cluster_assignment = self.optimize(distances_from_centroids,axis=1)
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

    def k_means_clustering(self):
        """
        Performs K-Means Clustering by iterating the steps of cluster assignment and centroid revision
        """
        self.centroids = self.get_initial_centroids()
        self.prev_cluster_assignment = None
        for itr in range(self.maxiter):
            print('ITERATION %s' %itr)
            self.cluster_assignment = self.assign_clusters()
            print('Finding new centroids')
            self.centroids = self.revise_centroids()
            print('Cluster reassignment')
            if self.prev_cluster_assignment is not None and (self.prev_cluster_assignment==self.cluster_assignment).all():
                #convergence check
                break
            if self.prev_cluster_assignment is not None:
                self.prev_cluster_assignment = self.cluster_assignment
        return self.centroids, self.cluster_assignment
