def zmiana_struktry(dna):
    dna = list(dna)
    for i in range(len(dna)):
        if dna[i] == "C":
            dna[i] = "*"
        elif dna[i] == "G":
            dna[i] = "*"
        elif dna[i] == "T":
            dna[i] = "*"
    dna = "".join(dna)
    print(dna)

zmiana_struktry("TGACCCA")