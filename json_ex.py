import json
d = {
    "name":"chandu",
    "age" :18
}
with open("data.json","w") as file:
    json.dump(d,file)

with open("data.json","r") as f:
    d = json.load(f)
print(d)
print(d["name"])