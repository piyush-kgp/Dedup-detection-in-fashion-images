`exact_duplicates.py` contains code for finding Product IDs with duplicate Image URLs. It contains code for pre-processing and a function to return a json file from a Pandas DataFrame in required format.

`download_images.py` contains code to download images and uses multiprocessing to speed up downloading; albeit leaving the machine extremely slow for several hours; but does significantly reduce the total download time. In a Virtual Machine setup; such code can be much more useful (because we wouldn't care for the usability of the machine in the meantime).

`KMeans.py` contains code to cluster images based on  a similarity measure.

`inception_features.py` contains code to extract 2048-dimensional features of images in batches of 1000 from Inception V3 network. We again resort to multiprocessing. Still it is extremely heavy for a machine with 4 GB RAM.

`find_duplicates_within_clusters.py` contains code to find duplicate images within a cluster (Using SSIM).

`combine_results.py` merges the two json files. It also contains a function to modularize merging JSONs.

`NOTE`: Clustering of 1.6L images will take too much time on my slow machine. So, for demo, only 10 images are used to cluster and report duplicates. The code can however be tested even with 10 images for consistency. This corresponds to the L21, L25-L31 on `KMeans.py` and L43-L47 on `find_duplicates_within_clusters.py`
Also I wanted to follow a similar process of clustering and finding duplicates for inception features but data size is too large to process. For this the same class can be used with variable optimize = `np.argmin` instead of `np.argmax`
