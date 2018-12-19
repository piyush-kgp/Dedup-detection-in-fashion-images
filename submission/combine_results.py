import json
from collections import defaultdict

def merge_jsons(json_files_to_merge, write_file, val_type = list):
    final_json = defaultdict(val_type)
    for json_file in json_files_to_merge:
        myjson = json.load(open(json_file, 'r'))
        for k, val in myjson.items():
            [final_json[k].append(v) for v in val]
    with open(write_file, 'w') as outfile:
        json.dump(final_json, outfile)

if __name__ == '__main__':
    merge_jsons(json_files_to_merge=['exact_duplicates.json', 'duplicates_within_clusters.json'],
                write_file='duplicate_product_ids.json')
