lista = []
for i in range(5):
    lista.append(int(input("Ingrese un número: ")))

lista2 = []

while len(lista2) < 5:
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    lista2.append(menor)
    lista.remove(menor)

print("Lista ordenada de menor a mayor:", lista2)