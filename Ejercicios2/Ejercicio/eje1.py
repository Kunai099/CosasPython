palabra1 = input("Ingresa una palabra o frase: ")
palabra2 = input("Ingresa otra palabra o frase: ")

p1 = palabra1.replace(" ", "").lower()
p2 = palabra2.replace(" ", "").lower()

if sorted(p1) == sorted(p2):
    print("Las palabras o frases son un anagrama")
else:
    print("No son un anagrama")

