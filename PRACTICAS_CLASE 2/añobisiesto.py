print("Determina si un año es bisiesto")
año = int(input("Introduce un año: "))
if (año % 400 == 0 and año % 100 != 0) or (año % 4 == 0 ):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")