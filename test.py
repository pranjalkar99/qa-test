import json
from tqdm import tqdm
with open('db4.json', 'r') as f:
    data = f.read()
lst = json.loads(data)
for index , dict in tqdm(enumerate(lst)):
    with open('jsons/db4_{}.json'.format(index),'w') as f:
        f.write(str(dict))
    f.close()
