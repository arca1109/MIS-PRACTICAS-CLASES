print("Hola, cálcula tu promedio de notas aquí")
cantidad_de_materias = int(input("Introduce la cantidad de materias que deseas promediar: "))
suma_de_notas = 0
for i in range(cantidad_de_materias):
    nota = float(input(f"Introduce la nota de la materia {i + 1}: "))
    suma_de_notas += nota
promedio = suma_de_notas / cantidad_de_materias
print(f"Tu promedio de notas es: {promedio:.2f}")