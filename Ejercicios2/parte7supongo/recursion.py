def numer(numero):
    if numero == 1000:
        return numero
    else:
        return numer(numero + 1)

print(numer(1))
