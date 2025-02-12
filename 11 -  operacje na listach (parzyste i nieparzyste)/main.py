#zdanie 1
listaa = [1,2,3,4,5,6,7,8,9,10]

# print("Podaj 10 wartości: ")
#
# for i in range(10):
#     a = input("Podaj liczbę: ")
#     lista.append(a)

def podzial(lista):

    liczby_parzyste = []
    liczby_nieparzyste = []

    for i in lista:
        if (i%2==0):
            liczby_parzyste.append(i)
        else:
            liczby_nieparzyste.append(i)

    print("Liczby parzyste: ", liczby_parzyste)
    print("Liczby nieparzyste: ", liczby_nieparzyste)

podzial(listaa)