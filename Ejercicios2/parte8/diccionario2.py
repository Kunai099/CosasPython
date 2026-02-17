def corregir_nota_python(alumnos):
    for estudiante, materias in alumnos.items():
        if "Python" in materias and materias["Python"] < 5:
            materias["Python"] = 5
