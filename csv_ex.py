import csv
d =[
    ["name","age"],
    ["chandu",21],
    ["kiran",20]
]
with open("data.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerows(d)