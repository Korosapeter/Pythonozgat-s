import json

with open ("monitor.json", encoding="UTF-8") as f:
    monitorok = json.load(f)

print("Üdvözlöm miben segíthetek?")
bekeres=(input("Monitor,Egér,Billentyűzet:"))
    

def választás(bekérés):
    if bekérés == "Monitor":
        print("Hány incses?")
        incs=int(input(""))
        for i in monitorok:
            for _ in i:
                print(i)
    
választás(bekeres)