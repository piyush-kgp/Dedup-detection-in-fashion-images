
import tensorflow_hub as hub
import cv2
import os
import numpy as np
import tensorflow as tf
import multiprocessing
import time
import os

img_dir = 'Images'
img_files = os.listdir(img_dir)
img_files = sorted(img_files)
chunks = [img_files[x:x+1000] for x in range(0, len(img_files), 1000)]
all_chunks = list(range(len(chunks)))
done_chunks = [int(x.split('_')[-1].split('.')[0]) for x in os.listdir() if x[-3:]=='npy']
undone_chunks = list(set(all_chunks)-set(done_chunks))

def inception_chunk(chunk_num):
    tit = time.time()
    bad=open('records/bad_product_ids_in_chunk_%s.txt' %chunk_num, 'a+')
    good=open('records/good_product_ids_in_chunk_%s.txt' %chunk_num, 'a+')
    img_stack = np.zeros((1000, 299, 299, 3))
    for i, img_file in enumerate(chunks[chunk_num]):
        try:
            img = cv2.imread(os.path.join(img_dir, img_file))
            img = cv2.resize(img, (299, 299))
            img_stack[i] = img
            good.write(img_file[:-4]+'\n')
        except:
            print('Check Image %s' %img_file)
            bad.write(img_file[:-4]+'\n')
            continue
    module = hub.Module("https://tfhub.dev/google/imagenet/inception_v3/feature_vector/1")
    features = module(img_stack)
    init_op = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init_op)
    my_feat = features.eval(session = sess)
    np.save('features/alphabetically_sorted_images_features_%s.npy' %chunk_num, my_feat)
    bad.close()
    good.close()
    tat = time.time()
    print('Chunk %s done in %s seconds' %(chunk_num, tat-tit))

pool = multiprocessing.Pool(processes = 2)
pool.map(inception_chunk, undone_chunks)
