import diccionario2 as d

estudiante1 = {
    "PSP" : 7,
    "Aceso a datos" : 5,
    "Python" : 2
}
estudiante2 = {
    "PSP" : 2,
    "Aceso a datos" : 7,
    "Python" : 8
}
estudiante3 = {
    "PSP" : 9,
    "Aceso a datos" : 3,
    "Python" : 6
}

alumnos = {
  "estudiante1" : estudiante1,
  "estudiante2" : estudiante2,
  "estudiante3" : estudiante3
}

print(alumnos)
d.corregir_nota_python(alumnos)
print(alumnos)
