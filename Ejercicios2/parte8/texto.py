def analizar_texto(texto):
    caracter = texto.__len__()
    palabras = texto.split()
    palabrasTot=palabras.__len__()
    primera=palabras[0]

    return (caracter, palabrasTot, primera)