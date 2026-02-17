contador = 0

try:
    numero = int(input("Introduce un numero: "))

    if numero > 0:
        for i in range(numero, 0, -1):
            if numero % i == 0:
                contador += 1

        if contador > 2:
            print("El numero no es primo")
        elif contador == 1:
            print("El uno no es primo")
        else:
            print("El numero es primo")
    else:
        print("Escribe un numero positivo")

except ValueError:
    print("Error: Debes introducir un número entero válido.")