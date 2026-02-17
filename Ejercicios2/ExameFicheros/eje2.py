with open("datos.txt") as f, open("limpio.txt", "w") as out:
    for line in f:
        if line.strip():
            out.write(line)