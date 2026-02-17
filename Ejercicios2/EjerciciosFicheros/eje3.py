palabra=input("Ingresa una palabra a buscar: ").lower()

try:
    with open("datoss.txt") as f:
        print(f.read().lower().count(palabra))

except FileNotFoundError:
    print("No existe el archivo")