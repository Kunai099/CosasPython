palabra=input("Ingrese una palabra: ")
with open("datos.txt") as f:
    texto=f.read()
    print(texto.count(palabra))