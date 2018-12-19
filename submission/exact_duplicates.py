import pandas as pd
import json

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


print('Number of times the word top appears in subcategory levels 1 to 6 =>',
      sum(large.subcategory_1.str.contains('top')), 
      sum(large.subcategory_2.str.contains('top')), 
      sum(large.subcategory_3.str.contains('top')), 
      sum(large.subcategory_4.str.contains('top')), 
      sum(large.subcategory_5.str.contains('top')), 
      sum(large.subcategory_6.str.contains('top')),
     )

large = large[large.subcategory_4.str.contains('top')]
print(large.shape)

def get_json_of_duplicates(df, key_col, val_col):
    """
    Returns a JSON exactly like required in the problem statement for exact matching
    Args: 
        df: A Pandas DataFrame Object,
        key_col: Key Column; the column whose entries will go into JSON, 
        val_col: Value column; the column whose values are compared to find duplicates
    Returns:
        A JSON with keys = first ID of each duplicated set of records and values = List of IDs corresponding to 
        the duplicated set of records for that key
    """
    df['dup_first'] = df.duplicated(subset = val_col, keep='first') #marks all duplicates as True except first entry
    df['dup_all'] = df.duplicated(subset = val_col, keep=False) #marks all duplicates as True
    mykeys = list(df[key_col][[not x for x in df.dup_first] & df.dup_all]) #First ID of each duplicated set of records
    def get_duplicates(k):
        return list(df[key_col][df[val_col].isin(df[val_col][df[key_col]==k])])[1:]
    return dict(zip(mykeys, [get_duplicates(k) for k in mykeys])) #what we want

# Test the function
df = pd.DataFrame({'idx': list('ABCDEFGHIJK'), 'val': list('xxyzzyxpqrx')})
temp_json
print(temp_json)

#Run function on real data and save results to file
# myjson = get_json_of_duplicates(large, key_col='productId', val_col='primaryImageUrlStr')
with open('exact_duplicates_temp.json', 'w') as outfile:
    json.dump(temp_json, outfile)