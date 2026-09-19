print("Calculadora de factorial")
while True:
    número = int(input("Ingresa un número entero no negativo: "))

    if número < 0:
        print("Error: El número no debe ser negativo.")
    else:
        factorial = 1
    for i in range(1, número + 1):
        factorial *= i
    print(f"El factorial de {número} es {factorial}")

    repetir = input("¿Deseas calcular otro factorial? (Sí o No): ")
    if repetir.lower() != "si":
        print("Gracias por usar la calculadora de factorial.")
        break