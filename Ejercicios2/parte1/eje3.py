try:
    nota=float(input("Ingrese la nota: "))
    if 0<=nota<=4.9:
        print("suspenso")
    elif 5<=nota<=6.9:
        print("aprobado")
    elif 7<=nota<=8.9:
        print("notable")
    elif 9<=nota<=10:
        print("sobresaliente")
    else:
        print("Error: la nota debe estar entre 0 y 10")
except:
    print("Error: la nota debe ser un numero")