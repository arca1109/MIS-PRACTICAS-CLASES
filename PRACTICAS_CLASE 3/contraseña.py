print("Crea una contraseña")

while True:
    longitud = int(input("Ingresa la longitud de la contraseña (mínimo 8 caracteres): "))
    if longitud < 8:
        print("Error: La longitud de la contraseña debe ser al menos 8 caracteres.")
    else:
        import random
        import string

        caracteres = string.ascii_letters + string.digits + string.punctuation
        contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
        print(f"Tu contraseña generada es: {contraseña}")

    repetir = input("¿Deseas generar otra contraseña? (Sí o No): ")
    if repetir.lower() != "si":
        print("Gracias por usar el generador de contraseñas.")
        break