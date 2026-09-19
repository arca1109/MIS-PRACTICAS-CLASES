print("Hola, cálcula aquí la canidad de segundos que hay en un tiempo determinado")
horas = int(input("Introduce la cantidad de horas: "))
minutos = int(input("Introduce la cantidad de minutos: "))
segundos = int(input("Introduce la cantidad de segundos: "))

tiempo_en_segundos = (horas * 3600) + (minutos * 60) + segundos

print(f"El tiempo total en segundos es: {tiempo_en_segundos} segundos")
