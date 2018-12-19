import pandas as pd
import os
import urllib
import threading

pd.set_option('display.max_colwidth', -1)
pd.set_option('display.max_columns', None)
large = pd.read_csv('large/2oq-c1r.csv')
print(large.shape)
large = large.drop_duplicates(subset='productId', keep="first")
print(large.shape)
large['primaryImageUrlStr'] = [str(item).split(';')[0] for item in large.imageUrlStr]
large['subcategory_levels'] = [str(item).split('>') for item in large['categories']]
large['n_levels'] = [len(item) for item in large.subcategory_levels]
large['subcategory_1'] = [item[0].lower() if len(item)>=1 else 'None' for item in large.subcategory_levels]
large['subcategory_2'] = [item[1].lower() if len(item)>=2 else 'None' for item in large.subcategory_levels]
large['subcategory_3'] = [item[2].lower() if len(item)>=3 else 'None' for item in large.subcategory_levels]
large['subcategory_4'] = [item[3].lower() if len(item)>=4 else 'None' for item in large.subcategory_levels]
large['subcategory_5'] = [item[4].lower() if len(item)>=5 else 'None' for item in large.subcategory_levels]
large['subcategory_6'] = [item[5].lower() if len(item)>=6 else 'None' for item in large.subcategory_levels]
large = large[large.subcategory_4.str.contains('top')]
print(large.shape)
large = large.drop_duplicates(subset='primaryImageUrlStr', keep="first")
print(large.shape)

def download_files(web_link, file_name):
    if os.path.isfile(file_name):
        pass
    else:
        try:
            urllib.request.urlretrieve(web_link, file_name)
        except:
            pass

urls = list(large.primaryImageUrlStr)
names = list('Images/'+ name.lower() +'.jpg' for name in large.productId)

thr = threading.Thread(taget = download_files, args = (urls, names,))
thr.start()
thr.join()
