def make_pizza(tamano, *ingredientes):

    if tamano < 1:
        res = "❌ No puedes escoger un tamaño negativo o cero"
    elif len(ingredientes) == 0:
        res = "❌ No puedes escoger una pizza sin ingredientes"
    else:
        lista_ingredientes = ", ".join(ingredientes)
        if tamano == 1:
            res = f"🍕 Una pizza de 1 porción con {lista_ingredientes}"
        else:
            res = f"🍕 Una pizza de {tamano} porciones con {lista_ingredientes}"

    return res