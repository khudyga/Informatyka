listaa = [1,5,2,7,8,9,5685,345,7,4,75674538,786,47,79]

def malejaco(lista):
    rozmiar = len(lista)

    for i in range(rozmiar):
        for j in range(rozmiar - i - 1):
            temp = lista[j]
            if lista[j] > lista[j + 1]:
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
    print(lista)

malejaco(listaa)