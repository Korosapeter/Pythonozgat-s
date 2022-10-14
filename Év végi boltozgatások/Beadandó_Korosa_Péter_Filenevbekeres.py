import json

lista = []
masik_lista = []

try:
    nev = input("Adjon meg egy file nevet")

    with open(nev ,"_") as fajl:
        fajl = json.load(fajl)

        fajl.split(" ")

    for i in fajl:
        lista.append(len(i))

    for i in lista:
        masik_lista.append(i)

    for i in lista:
        for i in lista:
            if lista.count(i) > 1:
                lista.remove(i)
                print(lista)

    for i in lista:
        print(i,"betűből áll",masik_lista.count(i),"db van.")
except FileNotFoundError:
    quit()
