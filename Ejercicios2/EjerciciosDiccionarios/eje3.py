frutas={
    "platano" : 1.35,
    "manzana" : 0.80,
    "pera" : 0.85,
    "naranja" : 0.70
}

elec=input("Elige una fruta: ").lower()
kil=float(input("Elige una cantidad en kilos: "))
try:
    precio=frutas[elec]*kil
    print(precio)

except KeyError:
    print("La fruta ingresada no existe en el diccionario")