osztandó=int(input("Adj meg egy számot"))
osztó=int(input("Adj meg egy számot"))
számolás=osztandó%osztó
if számolás ==1:
    print("A szám osztható maradék nélkül")
    print("Eredmény",számolás)
elif számolás ==0:
    print("a szám maradékos lesz")
    print("Eredmény",számolás)