import json
x={"name":"kyran","age":17,"hight":186}
y=json.dumps(x)
z=json.loads(y)
print(z)
print(z["name"])