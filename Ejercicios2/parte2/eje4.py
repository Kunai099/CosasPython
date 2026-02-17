try:
    saldo = int(input("Escribe el saldo inicial: "))

    if saldo <= 0:
        raise ValueError("El saldo no es válido. Debe ser mayor que 0.")

    retirar = int(input("Escribe la cantidad que desea retirar: "))

    if retirar <= 0:
        raise ValueError("La cantidad a retirar debe ser mayor que 0.")
    elif retirar > saldo:
        raise ValueError("No puedes retirar más dinero del que tienes en el saldo.")

    saldo = saldo - retirar
    print("El saldo nuevo es:", saldo)

except ValueError as e:
    if "invalid literal" in str(e):
        print("Error: Debes introducir solo números enteros.")
    else:
        print(e)

except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
