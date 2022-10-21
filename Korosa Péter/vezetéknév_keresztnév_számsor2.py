
honnan=int(input("Adj meg hogy honnan"))
meddig=int(input("Adj meg hogy meddig"))
hányasával=int(input("Adj meg hogy hányasával"))
for honnan,meddig,hányasával in range(5):

    for i in range(honnan,meddig,hányasával):
        print(i)
