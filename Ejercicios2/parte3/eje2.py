lista = []
total = 0
menor=None
mayor=None

while True:
    ent = input("Escribe un número (o 'done' para terminar): ")

    if ent.lower() == "done":
        break
    try:
        numero = int(ent)
        lista.append(numero)
    except ValueError:
        print("Error: Debes introducir un número entero válido.")

if len(lista) == 0:
    print("No se ingresaron números.")
else:

    for numero in lista:
        if menor is None or menor > numero:
            menor = numero
        if mayor is None or mayor < numero:
            mayor = numero
print("numero menor",menor)
print("numero mayor",mayor)