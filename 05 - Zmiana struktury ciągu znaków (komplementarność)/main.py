def zmiana_struktry(dna):
    dna = list(dna)
    for i in range(len(dna)):
        if dna[i] == "A":
            dna[i] = "T"
        elif dna[i] == "C":
            dna[i] = "G"
        elif dna[i] == "G":
            dna[i] = "C"
        elif dna[i] == "T":
            dna[i] = "A"
    dna = "".join(dna)
    print(dna[::-1])
zmiana_struktry("TGACCCA")