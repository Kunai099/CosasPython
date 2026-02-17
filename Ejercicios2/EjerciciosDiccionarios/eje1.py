monedas={
    "euro" : "€",
    "dollar" : "$",
    "yen" : "¥"
}

moneda=input("Ingresa una moneda: ").lower()

try:
    print (monedas[moneda])
except KeyError:
    print ("El valor ingresado no existe en el diccionario")