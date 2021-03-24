import random
plik = open('listaMnozona.txt', 'w+')
listaLosowa = []
nowaLista = []
for i in range(0,5):
    n = random.randint(0,30)
    listaLosowa.append(n)
print(listaLosowa)
mnozenie = 2

x = 2
for i in listaLosowa:
    nowaLista.append(x*i)
plik.writelines(str(nowaLista))
