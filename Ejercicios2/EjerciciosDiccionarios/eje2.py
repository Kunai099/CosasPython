nombre=input("Ingresa tu nombre: ")
edad=int(input("Ingresa tu edad: "))
direccion=input("Ingresa tu direccion: ")
telefono=input("Ingresa tu telefono: " )

persona={
    "nombre": nombre,
    "edad": edad,
    "direccion": direccion,
    "telefono": telefono
}

print(persona[nombre],"tiene",persona[edad],"años, vive en",persona[direccion],"y su número de teléfono es",persona[telefono])