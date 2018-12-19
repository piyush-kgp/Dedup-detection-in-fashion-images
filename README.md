
This project was about finding duplicate/very similar items in a large online fashion store.

Here we have used Scikit-Image's SSIM (Structural Similarity Measure) API to measure similarity.
`skimage.measure.compare_ssim`

During this project I wrote an algorithm for K-Means clustering with custom distance:
This is in the `KMeans` class at <KMeans.py>
This class takes a distance function in its initializer to calculate the distances at each iteration. We have used the `SSIM` as the distance function.

 I have also written code to calculate embeddings of images through `Inceptionv3` faster using multiprocessing. I have used Tensorflow Hub's `hub.module` API to calculate embeddings.

 Further ahead my plan was to find similarity using these embeddings.


##### Data
Data can be obtained from <https://huew.blob.core.windows.net/assignments/Assignment.html>. Raw data links:
<https://huew.blob.core.windows.net/assignments/2oq-c1r>
<https://huew.blob.core.windows.net/assignments/small-2oq-c1r.tar.gz>
