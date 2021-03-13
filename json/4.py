import json
x={
    "name":"kyran",
    "age":17,
    "weight":60
}
print(json.dumps(x,indent=4,sort_keys=True,separators=(". ","= ")))
