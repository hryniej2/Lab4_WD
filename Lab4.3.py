import sys

dodatek = "\nZycie\n zycie\n jest\n nobelom\n"

with open("listaMnozona.txt", "a+") as plik:
    plik.write(dodatek)
    for linia in plik:
        print(linia, end="")


with open("listaMnozona.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")