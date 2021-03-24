class Sklep:
    """Lista"""
    def __init__(self,nazwaProduktu, ilosc, jednostkaMiary, cena):
        self.nazwaProduktu = nazwaProduktu
        self.ilosc = ilosc
        self.jednostkaMiary = jednostkaMiary
        self.cena = cena
    def produkt(self):
        informacja = self.nazwaProduktu + "  ilosc: " + self.ilosc + " cena_jed: " + self.cena
        return informacja
    def ile(self):
        return self.ilosc + " " + self.jednostkaMiary
    def koszt(self):
        koszt = int(self.ilosc) * float(self.cena)
        return "Cena calosciowa to : " + str(koszt) + " zl"

marchewka = Sklep("marchewka","3","szt","2.5")

print(marchewka.produkt())
print(marchewka.ile())
print(marchewka.koszt())
