print("Determina cuál es el número mayor")
print("Introduce el calculo que deseas realizar")
def Comparacion (num1, num2):
    if num1 > num2:
        return f"El número {num1} es mayor que {num2}."
    elif num1 < num2:
        return f"El número {num2} es mayor que {num1}."
    else: 
        return f"Los números {num1} y {num2} son iguales."
num1 = int(input("Introduce el primer número:"))
num2 = int(input("Introduce el segundo número:"))

print(Comparacion(num1, num2))
