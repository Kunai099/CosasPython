try:
    numero1 = int(input("Ingresa un número: "))
    numero2 = int(input("Ingresa otro número: "))

    if numero1 > numero2:
        print("El número mayor es " + str(numero1))
    elif numero2 > numero1:
        print("El número mayor es " + str(numero2))
    else:
        print("Ambos números son iguales.")

except ValueError:
    print("Error: Debes introducir un número entero válido.")
