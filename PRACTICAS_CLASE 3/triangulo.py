print("Bienvenida al generador de Triángulos de números")
print("Crea un triángulo de números, según el número de filas que desees.")

while True:
    numero = int(input("Ingresa el número de filas: "))
    if numero <= 0:
            print("Error: El número de filas debe ser un entero positivo.")
    else:
        for i in range(1, numero + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()
    repetir = input("¿Deseas crear otro triángulo? (Sí o No): ")
    if repetir.lower() != "si":
        print("Gracias por usar el generador de triángulos de números.")
        break

