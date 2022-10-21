import random
Jancsi=[]
Juliska=[]
for i in range(1):
    dobás=random.randint(1,6)
    Jancsi.append(dobás)
print("Jancsi ennyit dobott")

for x in range(1):
    dobás=random.randint(1,6)
    Juliska.append(dobás)
print("Juliska ennyit dobott")
if Jancsi >Juliska:
    print("Jancsi nyert")
if Jancsi <Juliska:
    print("Juliska nyert")
if Jancsi ==Juliska:
    print("Jancsi nyert")
if Jancsi==6 & Juliska==6:
    print("Gratulálok")

