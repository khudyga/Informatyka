nominaly = [500, 200, 100, 50, 20, 10, 5, 2, 1]
kwota =  1899
i = 0
ile_razy = 0
while kwota > 0:
    if kwota > nominaly[i]:
        ile_razy = kwota // nominaly[i]
        kwota = kwota - nominaly[i] * ile_razy
        print(f"Nominał {nominaly[i]} został użyty {ile_razy}")
    else:
        i = i + 1

