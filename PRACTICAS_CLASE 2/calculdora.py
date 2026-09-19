print("Bienvenido a la calculadora")
print("Introduce el calculo que deseas realizar")
num1 = float(input("Introduce el primer número:"))
operación = input("Introduce el operador (+, -, *, /): ")
num2 = float(input("Introduce el segundo número:"))

if operación == "+":
    resultado = num1 + num2
elif operación == "-":
    resultado = num1 - num2
elif operación == "*":
    resultado = num1 * num2
elif operación == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: no se puede dividir entre 0"

print("Resultado:", resultado)







