
szam=int(input("Adj meg egy számot"))
szam1=int(input("Adj meg egy számot")) 
távolság =szam -szam1
if távolság==0:
    print("Egyenlő")
if távolság<=10:
    print("Nagyon közeli")
if távolság>10 & távolság <=30:
    print("átlagos távolság")
if távolság >=30:
    print("Távoli")