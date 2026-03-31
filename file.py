from pathlib import Path

name = input("what do you want to add on ")
data = input("what do you want to add on with some msg ")


p = Path (name)
if p.exists():
    print("file already exists")
else:
    file = open(p,"w")
    file.write(data)

with open("" , 'r') as f:
    print(f.read())
