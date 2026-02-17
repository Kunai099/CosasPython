compra = {}
seguir = True
total=0

while seguir:
    producto = input("Ingrese el producto que quieres comprar: ")
    precio = input("Ingrese el precio: ")

    compra[producto] = precio

    seguir2 = input("¿Quieres seguir? (si/no): ").lower()
    if seguir2 == "no":
        seguir = False

print("Compra completa")
for x in compra:
    print(x,"-----------",compra[x])
    total += float(compra[x])

print("Precio total: ",total)