def znajdz_wzorzec(tekst, wzorzec):
    counter = 0
    dlugosc_tekstu = len(tekst)
    dlugosc_wzorca = len(wzorzec)

    for i in range(dlugosc_tekstu-dlugosc_wzorca+1): #do momentu dopoki istnieje po prawej tyle znakow ile we wzorcu.
        for j in range(dlugosc_wzorca): #sprawdzamy w danym odcinku czy znaki sa sobie rowne
            if tekst[i+j] != wzorzec[j]: # normalnie liczymy od j ale trzeba dodac i bo jak nie znajdzie w danym odcinku o dlugosci wzorca podanego wzorca to idzie od razu dalej???
                break
        else: #jakas upo instrukcja else do for????
            print(f"Znaleziono wzorzec {wzorzec} na pozycji {i}")
            counter += 1

    if counter == 0:
        print("Nie ma podanego wzorca w tekscie.")
    else:
        print(f"Wzorzec {wzorzec} występuje w tekście {tekst} {counter} razy ")

znajdz_wzorzec("matematyka", "a")