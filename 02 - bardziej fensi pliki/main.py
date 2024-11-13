
# r - odczytywanie
# w - zapisywanie
# a - dodawanie do istniejacego
# plik.read() - czytanie
# plik.write() - wpisywanie


#1
odczytywanie = open("odczytywanie.txt", "r")
zawartosc = odczytywanie.read()
print(zawartosc)
odczytywanie.close()

#2
odczytywanie2 = open("odczytywanie2.txt")
zawartosc2 = odczytywanie2.readline()
print(zawartosc2) #wypisuje tylko 1 linie
odczytywanie2.close()

#3 odczytywanie wszystkiego readline petla zeby nie zajmowac pamieci
odczytywanie3 = open("odczytywanie3.txt")
for linia in odczytywanie3:
    print(linia)
    # end=""pusty znak konca linii zeby sie nie robila taka brzydka przerwa
odczytywanie3.close();

#lepsze otwieranie i automatycznie zamykanie
#zapisywanie do pliku
with open("odczytywanie4.txt", "w") as odczytywanie4:
    odczytywanie4.write("Super informacja")

with open("odczytywanie4.txt", "r") as odczytywanie4:
    for linia in odczytywanie4:
        print(linia)

#kopiowanie z jednego do drugiego pliku
with open("kopiowanie.txt", "r") as kopiowanie:
    with open("wklejanie.txt", "w") as wklejanie:
        for linia in kopiowanie:
            wklejanie.write(linia)

#kowertowanie do int -> wklejanie.write(int(linia))
# \n - nowa linia
#\t - tabulator
