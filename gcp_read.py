from google.cloud import storage
from google.oauth2 import service_account
import os
import json
import random
from tqdm import tqdm
storage_cleint = storage.Client.from_service_account_json('compfox-367313-ad58ca97af3b.json')
def name_split(filename):
    # split the filename by underscore
    parts = filename.split('_')

    # extract the required substring
    name = parts[3][:-4]
    return name
#client = storage.Client(Credentials=google_credentials)
bucket_name = "regular_final_html"
print('writing the json file ......')
# Get a reference to the bucket
bucket = storage_cleint.get_bucket(bucket_name)
# List all HTML files in the bucket
blobs = bucket.list_blobs(prefix="", delimiter="/")
filenames = []
names = []
dict_list = []
missing_file = []
keys = []
data = {}
for blob in tqdm(blobs,ascii=True):
    if blob.name.endswith('.pdf'):
        filenames.append(blob.name)
for file in tqdm(set(filenames)):
    name = name_split(file)
    names.append(name)
    html_blob = bucket.blob(file)
    html_contents = html_blob.download_as_string().decode("utf-8")
    try:
        my_dict = json.loads(html_contents)
    except json.decoder.JSONDecodeError as e:
        missing_file.append(file)
        print("Error decoding JSON: in file : {}".format(file), str(e))

    for key, value in my_dict.items():
        keys.append(key)
        id = random.randint(0,5000000)
        data[id] = {"text": value, "filename":name}
        if len(keys)>100:
            dict_list.append(data)
            keys = []
            data = {}

dict_list.append(data)
# convert the list to JSON
json_data = json.dumps(dict_list)
#
with open('db4.json', 'w') as h:
    h.write(json_data)
# # save the JSON data to a file
with open('names.txt', 'w') as f:
     f.write(str(names))
with open('filename.txt','w') as p:
    p.write(str(filenames))
with open('missingfile.txt','w') as x:
    x.write(str(missing_file))
h.close()
f.close()
p.close()
x.close()
