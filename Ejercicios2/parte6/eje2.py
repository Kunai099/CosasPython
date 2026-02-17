while True:
    try:
        numero = int(input("Escribe un número entero positivo: "))
        if numero >= 1:
            break
        else:
            print("Número no válido. Debe ser mayor o igual a 1.")
    except ValueError:
        print("Debes escribir un número entero válido.")

for i in range(numero, 0, -1):
    if i !=1:
        print(i, end=", ")
    else:
        print(i)