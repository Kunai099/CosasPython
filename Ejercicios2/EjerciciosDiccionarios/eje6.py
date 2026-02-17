paciente = {}
seguir = True

while seguir:
    clave = input("Ingrese el dato que quiere añadir (nombre, edad, etc.): ")
    valor = input("Ingrese el valor: ")

    paciente[clave] = valor
    print("Datos actuales del paciente:", paciente)

    seguir2 = input("¿Quieres seguir? (si/no): ").lower()
    if seguir2 == "no":
        seguir = False
