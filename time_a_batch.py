
import tensorflow_hub as hub
import cv2
import os
import numpy as np
import tensorflow as tf
import multiprocessing
import time

tit = time.time()
img_dir = 'Images'
img_files = os.listdir(img_dir)
img_files = sorted(img_files)
chunks = [img_files[x:x+1000] for x in range(0, len(img_files), 1000)]

chunk_num = 1
img_stack = np.zeros((1000, 299, 299, 3))
for i, img_file in enumerate(chunks[chunk_num]):
    img = cv2.imread(os.path.join(img_dir, img_file))
    img = cv2.resize(img, (299, 299))
    img_stack[i] = img

module = hub.Module("https://tfhub.dev/google/imagenet/inception_v3/feature_vector/1")
features = module(img_stack)
init_op = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init_op)
my_feat = features.eval(session = sess)
np.save('alphabetically_sorted_images_features_%s.npy' %chunk_num, my_feat)
tat = time.time()
print('Chunk %s done in %s seconds' %(chunk_num, tat-tit))
