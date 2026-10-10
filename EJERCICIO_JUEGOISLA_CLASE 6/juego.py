from datos import cargar_escenas, buscar_escena, guardar_estado_partida
from mecanicas import procesar_cambios_escena, agregar_objeto, validar_requesito
import pandas as pd

def iniciar_juego():
    df_escenas = cargar_escenas("escenas_isla.xlsx")
    if df_escenas is None:
        return

    # Estado inicial del jugador
    escena_actual = "inicio"
    inventario = []
    salud = 100
    hambre = 0
    dia = 1
    juego_activo = True

    estado_jugador = {
        "salud": salud,
        "hambre": hambre,
        "dia": dia
    }

    print("🌴 ¡BIENVENIDO A LA AVENTURA EN LA ISLA PERDIDA! 🌴\n")

    while juego_activo:
        escena = buscar_escena(df_escenas, escena_actual)
        
        if escena is None:
            print(f"❌ Error: La escena '{escena_actual}' no existe.")
            break

        # Mostrar estado actual del jugador
        print("=" * 50)
        print(f"📅 Día: {estado_jugador['dia']} | ❤️ Salud: {estado_jugador['salud']}% | 🍖 Hambre: {estado_jugador['hambre']}%")
        if inventario:
            print(f"🎒 Inventario: {', '.join(inventario)}")
        print("=" * 50)

        print(f"\n📍 Ubicación: {escena['id_escena'].upper()}")
        print(f"\n{escena['descripcion']}")

        # Validar si el jugador se quedó sin salud
        if estado_jugador['salud'] <= 0:
            print("\n💀 Te has quedado sin salud. No lograste sobrevivir.")
            guardar_estado_partida(escena_actual, inventario, "malo")
            break

        # Verificar si es una escena final
        es_final = str(escena['es_final']).strip().lower() in ['true', '1', 'si', 'yes']
        if es_final:
            print(f"\n🏁 {escena['mensaje_final']}")
            guardar_estado_partida(escena_actual, inventario, escena.get('tipo_final'))
            break

        # Opciones de acción
        opciones_disponibles = {}

        print("\nOpciones de acción:")
        
        # Opción A
        if pd.notna(escena['opcion_a']) and str(escena['opcion_a']).strip() != "":
            req_a = escena.get('requiere_objeto')
            if pd.isna(req_a) or str(req_a).strip() == "" or req_a in inventario:
                opciones_disponibles['a'] = {
                    'texto': escena['opcion_a'],
                    'destino': escena['destino_a']
                }
                print(f"  [A] {escena['opcion_a']}")
            else:
                print(f"  [X] {escena['opcion_a']} 🔒 (Requiere: {req_a})")

        # Opción B
        if pd.notna(escena['opcion_b']) and str(escena['opcion_b']).strip() != "":
            opciones_disponibles['b'] = {
                'texto': escena['opcion_b'],
                'destino': escena['destino_b']
            }
            print(f"  [B] {escena['opcion_b']}")

        if not opciones_disponibles:
            print("\nNo hay más caminos disponibles. Fin de la aventura.")
            break

        # Leer selección del usuario
        eleccion = input("\n👉 Selecciona una opción (A/B): ").strip().lower()

        if eleccion in opciones_disponibles:
            # Procesar cambios en estadísticas y objetos
            procesar_cambios_escena(escena, estado_jugador)
            agregar_objeto(inventario, escena)

            # Actualizar escena actual
            escena_actual = opciones_disponibles[eleccion]['destino']
        else:
            print("\n❌ Opción inválida. Por favor, elige una opción correcta.")

    print("\n¡Gracias por jugar!")

if __name__ == "__main__":
    iniciar_juego()