import pizza as p

pedidos = [
    (5, "tomate", "salchicha", "piña", "queso"),
    (1, "queso", "jamón"),
    ("dos",),
    (0,),
    (3,)
]

for pedido in pedidos:
    try:
        print(p.make_pizza(*pedido))

    except ValueError:
        print("Error: El tamaño de la pizza debe ser un número entero positivo.")

    except TypeError:
        print("Error: Los argumentos proporcionados no son válidos para hacer una pizza.")