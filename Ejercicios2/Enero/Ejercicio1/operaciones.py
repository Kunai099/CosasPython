def cuentavocales(cadena):
    cadena = cadena.lower()

    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0

    for letra in cadena:
        if letra == "a" or letra == "á":
            contadorA += 1
        elif letra == "e" or letra == "é":
            contadorE += 1
        elif letra == "i" or letra == "í":
            contadorI += 1
        elif letra == "o" or letra == "ó":
            contadorO += 1
        elif letra == "u" or letra == "ú":
            contadorU += 1

    listaVocales = {
        "a" : contadorA,
        "e" : contadorE,
        "i" : contadorI,
        "o" : contadorO,
        "u" : contadorU
    }

    mostrar(listaVocales)

def mostrar(listaVocales):
    for vocal, cantidad in listaVocales.items():
        if cantidad == 1:
            print(f"La vocal {vocal} aparece 1 vez")
        else:
            print(f"La vocal {vocal} aparece {cantidad} veces")
