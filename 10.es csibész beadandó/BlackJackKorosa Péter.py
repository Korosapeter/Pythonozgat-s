import random

pakli=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

saját = []
for i in range(2):
    lap = random.choice(pakli)
    saját.append(lap)
összeg = saját[0] + saját[1]
print("a lapjaid", saját)
print(összeg)

osztó = []
for i in range(2):
    lap = random.choice(pakli)
    osztó.append(lap)
osztó_összeg = osztó[0] + osztó[1]
print("osztó lapjai", osztó[0] + osztó[1])
flag =1
if összeg == 21:
    print("Black Jacked van.NYERTÉL")
elif összeg < 21:
    while flag ==1:
        saját_kérés=input("válassz: kérsz vagy megállsz")
        if saját_kérés =="kérsz":
            lap=random.choice(pakli)
            saját.append(lap)
            print(saját)
            összeg = sum(saját)
            print(összeg)
            if összeg >21:
                print("Vesztettél")
                flag = 0
            elif összeg == 21:
                print("nyertél")
                flag=0
            elif összeg <21:
                flag = 1
        elif saját_kérés =="megállsz":
            if osztó_összeg <17:
                lap1 = random.choice(pakli)
                osztó.append(lap1)
                osztó_összeg = sum(osztó)
            if összeg > osztó_összeg :
                print("Nyertél")
                print(osztó_összeg)
                flag=0
            elif összeg < osztó_összeg:
                print("Vesztettél")
                print(osztó,osztó_összeg)
                flag=0