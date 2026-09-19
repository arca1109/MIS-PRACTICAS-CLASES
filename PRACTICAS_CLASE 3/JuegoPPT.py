import random

print ("Bienvenido al juego de piedra, papel o tijera")
print ("Elige una opción")
OPCIONES = ["piedra", "papel", "tijera"]

while True:
    OPCIÓN = input("Tu elección: (piedra, papel o tijera): ").lower()
    if OPCIÓN not in OPCIONES: 
        print ("Opción inválida.")
        continue
     
    COMPUTADORA = random.choice(OPCIONES)
    print (f"Tu elección: {OPCIÓN}")
    print (f"La computadora elige: {COMPUTADORA}")

    if OPCIÓN == COMPUTADORA:
        print ("¡Empate!")
        JUGARDENUEVO = input("¿Quieres seguir jugando? (Sí o No): ")
        if JUGARDENUEVO.lower() == "no":
            print ("Gracias por jugar.")
            break
    elif (OPCIÓN == "piedra" and COMPUTADORA == "tijera") or\
         (OPCIÓN == "papel" and COMPUTADORA == "piedra") or\
         (OPCIÓN == "tijera" and COMPUTADORA == "papel"):
        print ("¡Felicidades! Has ganado.")
    else:
        print ("¡Lo siento! Has perdido.")

    JUGARDENUEVO = input("¿Quieres jugar de nuevo? (Sí o No): ")
    if JUGARDENUEVO.lower() == "no":
                print ("Gracias por jugar.")
                break