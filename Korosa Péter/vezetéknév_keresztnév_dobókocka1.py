import random
szám=[]
dobás=int(input("Add meg hogy hámyszor akarsz dobin"))
for i in range(dobás):
    dobások=random.randint(0,6)*dobás
print(dobások)
szám.append(dobások)
egy= szám.count(1)
print("ennyi eggyes van",egy)

hat=szám.count(6)
print("ennyi hatos van",hat)