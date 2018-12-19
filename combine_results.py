import json
from collections import defaultdict

def merge_jsons(file1, file2, write_file, val_type = list):
    final_json = defaultdict(val_type)
    json1 = json.load(open(file1, 'r'))
    json2 = json.load(open(file2, 'r'))
    for k, v in json1.items():
        final_json[k].append(v)
    for k, v in json2.items():
        final_json[k].append(v)
    with open(write_file, 'w') as outfile:
        json.dump(final_json, outfile)

if __name__ == '__main__':
    merge_jsons('exact_duplicates.json', 'duplicates_within_clusters.json', 'duplicate_product_ids.json')
