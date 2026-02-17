lista = []
total = 0

while True:
    try:
        ent = input("Escribe un número (o 'done' para terminar): ")

        if ent.lower() == "done":
            break

        numero = int(ent)
        lista.append(numero)

    except ValueError:
        print("Debes introducir un número entero válido.")

if len(lista) == 0:
    print("No se ingresaron números.")
else:
    total = sum(lista)
    promedio = total / len(lista)

    print("Suma total:", total)
    print("Cantidad de números ingresados:", len(lista))
    print("Promedio:", promedio)
