
This project was about finding duplicate/very similar items in a large online fashion store.

Here we have used Scikit-Image's SSIM (Structural Similarity Measure) API to measure similarity.
`skimage.measure.compare_ssim`

##### SSIM definition:
$SSIM(x,y) = {\frac  {(2\mu _{x}\mu _{y}+c_{1})(2\sigma _{{xy}}+c_{2})}{(\mu _{x}^{2}+\mu _{y}^{2}+c_{1})(\sigma _{x}^{2}+\sigma _{y}^{2}+c_{2})}}$


$\mu _{x}$, the average of  x;
$\mu _{y}$, the average of y;
$\sigma_{x}^2$, the variance of x
$\sigma_{y}^2$, the variance of y
$\sigma_{xy}$, the covariance of x, y
$c_1 = (k_1L)^2, c_2 = (k_2L)^2$,  two variables to stabilize the division with weak denominator
$L$, the dynamic range of the pixel-values
$k_1 = .01, k_2 = .03$, by default

During this project I wrote an algorithm for K-Means clustering with custom distance:
This is in the `KMeans` class at <KMeans.py>
This class takes a distance function in its initializer to calculate the distances at each iteration. We have used the `SSIM` as the distance function.

 I have also written code to calculate embeddings of images through `Inceptionv3` faster using multiprocessing. I have used Tensorflow Hub's `hub.module` API to calculate embeddings.

 Further ahead my plan was to find similarity using these embeddings.
