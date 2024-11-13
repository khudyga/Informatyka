#w - wpisywanie od poczatku, wszystko sie zeruje
#r - zczytywanie
#a - dodawanie do istniejacej zawartosci


#otwieranie pliku do zapisu
file1 = open("test.txt", "a", encoding="utf-8") #plik utworzy sie sam jak nie jest utworzony + polskie znaki

#ZAPISYWANIE DANYCH DO PLIKU
print(file1.writable()) #sprawdza czy jest do zapisu true/false

#wpisywanie do pliku tego co wprowadzi użytkownik
#!!!!!!!!!!!!!! ZNACZNIK NOWEJ LINII -> \n
file1.write(input("Co chcesz wpisać?" + "\n") + "\n")

#zamykanie i zwalnianie pamieci
file1.close()

#WYCZYTYWANIE DANYCH Z PLIKU
file1 = open("test.txt", "r", encoding="utf-8")

print(file1.readable()) #sprawdza czy jest do odczytu true/false

#przepisywanie tego co jest w file1 do zmiennej
# tekst = file1.read()
#
# print(tekst)

#kazda linijka jest zapisywana jako element listy
tekst2 = file1.readlines()
print(tekst2[1]) #wyczytuje tylko 2 linijke

#TO NIE DZIAŁA BO JEST UPO

# Problem polega na tym, że po użyciu metody readlines() wskaźnik odczytu w pliku zostaje przesunięty na jego koniec. Oznacza to, że kiedy później próbujesz ponownie przejść przez plik w pętli for linijka in file1, Python nie widzi już żadnych danych, ponieważ jest na końcu pliku.

#petla do wypisywania wszystkich linii jak nie chcemy zwyklego printa
if file1.readable():
    for linijka in file1:
        print(linijka)
        #KAZDA L TO JEDNA LINIA!!
