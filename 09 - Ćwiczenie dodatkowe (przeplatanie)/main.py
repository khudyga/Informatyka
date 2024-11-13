def przeplatanie(tekst):
    tekst2 = tekst[::-1]
    tekst3 = []
    tekst = list(tekst)
    tekst2 = list(tekst2)
    for i in range(len(tekst)):
        tekst3.append(tekst[i])
        tekst3.append(tekst2[i])
    tekst3 = "".join(tekst3)
    print(tekst3)

przeplatanie("azalia")
