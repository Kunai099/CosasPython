import random

def ganador(*participantes):
    if len(participantes) == 0:
        return "No hay participantes en la carrera"
    else:
        indice = random.randint(0, len(participantes) - 1)
        gana = participantes[indice]
        return f"El ganador es: {gana} "
