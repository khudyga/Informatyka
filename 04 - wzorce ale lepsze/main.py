def znajdz_wzorzec(tekst, wzorzec):
    counter = 0
    dlugosc_tekstu = len(tekst)
    dlugosc_wzorca = len(wzorzec)

    for i in range(dlugosc_tekstu-dlugosc_wzorca+1): #do momentu dopoki istnieje po prawej tyle znakow ile we wzorcu.
       if tekst[i] == wzorzec[0]:
           if tekst[i:i+dlugosc_wzorca] == wzorzec: #to jest git
               print(f"Znaleziono wzorzec {wzorzec} w tekscie {tekst} na pozycji {i}")
               counter += 1
           else:
               print("Nie znaleziono wzorca.")

    if counter == 0:
        print("Nie ma podanego wzorca w tekscie.")
    else:
        print(f"Wzorzec {wzorzec} występuje w tekście {tekst} {counter} razy ")

znajdz_wzorzec("matematyka", "a")