contador = 0
lista = []

try:
    numero = int(input("Introduce un número: "))

    if numero > 1:
        for j in range(2, numero + 1):
            contador = 0
            for i in range(1, j + 1):
                if j % i == 0:
                    if contador > 2:
                        break
                    else:
                        contador += 1
            if contador == 2:
                lista.append(j)

        print("Números primos hasta", numero, ":")
        for primo in lista:
            print(primo)
    else:
        print("Escribe un número mayor que 1")

except ValueError:
    print("Error: Debes introducir un número entero válido.")
