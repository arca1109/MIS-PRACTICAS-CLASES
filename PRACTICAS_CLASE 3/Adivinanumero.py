import random
numero_secreto = random.randint(1, 100)

print("Bienvenido al juego de adivinar el número")
print("¿Te atreves a adivinar el número que he pensado?")

while True:
    intento = int(input("Introduce tu número: "))
    if intento < numero_secreto: 
        print("Tu número está por DEBAJO.")
    elif intento > numero_secreto:
        print("Tu número está por ARRIBA")
    else:
        print("¡Has acertado! ¡FELICIDADES!")
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (Sí o No): ")
        if jugar_de_nuevo.lower() == "sí":
            numero_secreto = random.randint(1, 100)
        else:
            print("Gracias por jugar.")
            break