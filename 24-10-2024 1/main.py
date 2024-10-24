#otwieranie pliku
#f = open("plik.txt")

#r - read
#w - write
#a - append
with open("plik.txt", "r") as file:
    dane = file.read()
    print(dane)

#alternatywnie -> for linia in dane: print(linia, end="")

# to automatycznie zamyka wiec nie trzeba używać file.close()

#aby wypisac trzeba najpierw przeczytac dany plik

#zapisywanie do pliku
with open("zapis.txt", "w") as file:
    file.write("Jakis super tekst")

#kopiowanie jednego do drugiego pliku
with open("plik.txt", "r") as file1:
    with open("kopiowanie.txt", "w") as file2:
        for line in file1:
            file2.write(line)


#wyczytywanie danych skopiowanych do innego pliku
with open("kopiowanie.txt", "r") as filee:
    for line in filee:
        print(line)
        #nie trzeba otwierac drugi raz w odczytywaniu jak robimy petle
        # wszystko jest zapisywane jako string

#zapisywanie ciągu liczb do pliku
with open("liczby.txt", "w") as file:
    for i in range(1,11):
        file.writelines(str(i))

with open("liczby.txt", "r") as file:
    for line in file:
        print(line)


#zapisywanie do pliku skopiowanych danych z innego, ale tylko tych podzielnych przez 2


