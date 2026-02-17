while True:
    try:
        inver = float(input("Escribe la cantidad a invertir: "))
        interes = float(input("Escribe el interés anual (en %): "))
        anios = int(input("Escribe el número de años: "))
        break
    except ValueError:
        print("Debes introducir números válidos. Intenta de nuevo.\n")

for i in range(1, anios + 1):
    capital = inver * (1 + interes / 100) ** i
    print(f"Año {i}: capital = {capital:.2f} €")
