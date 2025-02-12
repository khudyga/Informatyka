lista = [1,2,3,4,5,6,7,8,9,0]

def pierwsza(lista):
    rozmiar = len(lista)
    for i in range(rozmiar - 1):
        if lista[i]%2==0:
            continue
        else:
            lista[i] = 1
    print(lista)

pierwsza(lista)