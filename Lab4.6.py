class Robaczek:
    def __init__(self, x, y ,krok):
        self.x = int(x)
        self.y = y
        self.krok = krok
    def gora(self):
        y1 = int(self.y) + int(self.krok)
        info = "Wspolrzedne to: " + str(self.x) + "," + str(y1)
        return info
    def dol(self):
        y2 = int(self.y) - int(self.krok)
        info =  "Wspolrzedne to: " + x + "," + str(y2)
        return info
    def prawo(self):
        x1 = int(self.x) + int(self.krok)
        info = "Wspolrzedne to: " + str(x1) + "," + y
        return info
    def lewo(self):
        x2 = int(self.x) - int(self.krok)
        info = "Wspolrzedne to: " + str(x2) + "," + y
        return info
    def gdzieTy(self):
        info = x + "," + y
        return info


x = input("Podaj wspolrzedna x: ")
y = input("Podaj wspolrzedna y: ")
krok = input("Podaj o ile krokow Robaczek ma sie przemiescic: ")

robaczek = Robaczek(x,y,krok)

print(robaczek.gora())
print(robaczek.lewo())