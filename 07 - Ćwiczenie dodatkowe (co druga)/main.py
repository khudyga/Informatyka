# This is a sample Python script.
def co_druga(tekst):
    tekst = list(tekst)
    for i in range(len(tekst)):
        if i % 2:
            tekst[i]=""
    tekst = "".join(tekst)
    print(tekst)

co_druga("aksamitka")