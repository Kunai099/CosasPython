try:
    edad = input("Ingrese su edad (solo se aceptarán números enteros positivos): ")
    edad = int(edad)

    if edad < 0:
        print("Error: la edad no puede ser negativa.")
    elif edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")

except ValueError:
    print("Error: Debes introducir un número entero válido.")
