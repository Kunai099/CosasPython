estadisticaBas=2

guerrero = {
    "ataque" : estadisticaBas,
    "alcance" : estadisticaBas,
    "defensa" : estadisticaBas,
    "vida" : estadisticaBas
}

caballero = {
    "ataque" : guerrero["ataque"]/2,
    "alcance" : guerrero["alcance"]/2,
    "defensa" : guerrero["defensa"]*2,
    "vida" : guerrero["vida"]*2
}

arquero = {
    "ataque" : guerrero["ataque"],
    "alcance" : guerrero["alcance"]*2,
    "defensa" : guerrero["defensa"]/2,
    "vida" : guerrero["vida"]
}

clases = {
    "guerrero" : guerrero,
    "caballero" : caballero,
    "arquero" : arquero,
}

print(clases)