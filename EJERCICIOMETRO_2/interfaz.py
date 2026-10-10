from Estacionesmetro import estaciones_metro
# Importamos el mapa, el calculador y los prints de tu planificador
from planificador2 import construir_grafo, calcular_ruta_optima, mostrar_reporte_pantalla

def ejecutar_interfaz():
    # 1. Preparamos el mapa inteligente con todas tus reglas
    mapa_metro = construir_grafo(estaciones_metro)
    
    # Creamos un conjunto de nombres válidos para verificar de forma simple
    nombres_validos = set(nodo[0] for nodo in mapa_metro.keys())

    print("=" * 50)
    print("🚇 INTERFAZ INTERACTIVA DEL METRO 🚇")
    print("=" * 50)
    print("Puedes escribir en minúsculas (ej: propatria, la hoyada)\n")
    
    # 2. Pedir datos y convertirlos automáticamente al formato de la Base de Datos
    origen = input("📍 Ingrese la estación de ORIGEN: ").strip().title()
    while origen not in nombres_validos:
        print("❌ Esa estación no existe en el sistema. Intente de nuevo.")
        origen = input("📍 Ingrese la estación de ORIGEN: ").strip().title()
        
    destino = input("\n🏁 Ingrese la estación de DESTINO: ").strip().title()
    while destino not in nombres_validos:
        print("❌ Esa estación no existe en el sistema. Intente de nuevo.")
        destino = input("🏁 Ingrese la estación de DESTINO: ").strip().title()
    
    # 3. Calcular la ruta con tu lógica de grafos
    resultado = calcular_ruta_optima(origen, destino, mapa_metro)
    
    # 4. Llamamos a los prints del otro archivo. ¡Cero código repetido!
    print("\nCalculando itinerario interactivo...")
    mostrar_reporte_pantalla(origen, destino, resultado)

if __name__ == "__main__":
    ejecutar_interfaz()