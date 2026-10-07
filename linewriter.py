STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "

def writeTextToFile(dodatek):
    vysledny_text = STATICKY_TEXT + str(dodatek)
    jmeno_souboru = "muj_soubor.txt"
    with open(jmeno_souboru, "w") as soubor:
        soubor.write(vysledny_text)
    return jmeno_souboru