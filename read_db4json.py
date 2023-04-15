import json
with open('db4.json','r') as f:
    data = f.read()
df = json.loads(data)
x = json.dumps(df[0])
with open('test.json','w') as p:
    p.write(x)
p.close()
f.close()
