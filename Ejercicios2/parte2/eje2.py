try:
    dinero = float(input("Escribe la cantidad en euros: "))

    if dinero > 0:
        divisa = input("Escribe la divisa (USD, GBP, JPY): ").upper()

        if divisa == "USD":
            dinero = dinero * 1.17
            print(f"La cantidad en dólares estadounidenses (USD) es: {dinero:.2f}")
        elif divisa == "GBP":
            dinero = dinero * 0.87
            print(f"La cantidad en libras esterlinas (GBP) es: {dinero:.2f}")
        elif divisa == "JPY":
            dinero = dinero * 176.07
            print(f"La cantidad en yenes japoneses (JPY) es: {dinero:.2f}")
        else:
            print("Error: Divisa incorrecta. Solo se aceptan USD, GBP o JPY.")
    else:
        raise ValueError("Error: La cantidad debe ser mayor que 0.")

except ValueError:
    print("Error: Debes introducir una cantidad numérica válida.")

