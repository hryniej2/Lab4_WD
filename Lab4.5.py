class ciagArytmetyczny:
    """ElementyCiagu"""
    def __init__(self, a1, r, an):
        self.a1 = a1
        self.r = r
        self.an = an
    def wyswietl(self):
        info = "Dane to: pierwszy wyraz wynosi :" + self.a1 + " ,a roznica wynosi : " + self.r
        return info
    def wartosci(self):
        an = int(self.a1) + (int(self.an) - 1) * int(self.r)
        info = "Wyraz " + self.an + " wynosi: " + str(an)
        return info
    def suma(self):
        suma = 0.5 * ((2 * int(self.a1) + ((int(self.an) -1 )) * int(self.r)) * int(self.an))
        info = "Suma wynosi: " + str(suma)
        return info

a = input("Podaj pierwszy wyraz: ")
b = input("Podaj roznice: ")
c = input("Podaj, ktory wyraz chcesz obliczyc: ")
ciag = ciagArytmetyczny(a,b,c)
print(ciag.wyswietl1())
print(ciag.wartosci())
print(ciag.suma())
