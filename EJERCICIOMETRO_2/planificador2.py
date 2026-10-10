import random
from Estacionesmetro import estaciones_metro

def construir_grafo(datos_metro):
    """
    Construye el mapa del metro conectando las estaciones de la misma línea.
    Usa el random.randint de la base de datos como el tiempo de túnel simétrico (ida y vuelta).
    """
    grafo = {}
    
    # 1. Agrupar las estaciones por Línea manteniendo su orden físico y su tiempo asignado
    lineas_separadas = {}
    for estacion in datos_metro:
        nombre = estacion[0]
        tiempo_tunel = estacion[1] # Este es tu random.randint(1, 5)
        info = estacion[2]
        linea_ppal = info[0] # La primera posición siempre es la línea actual
        
        if linea_ppal not in lineas_separadas:
            lineas_separadas[linea_ppal] = []
        
        # Guardamos la estación con su tiempo hacia la siguiente
        lineas_separadas[linea_ppal].append((nombre, tiempo_tunel, info))

    # 2. Conectar estaciones contiguas dentro de cada línea de forma aislada
    for nombre_linea, lista_estaciones in lineas_separadas.items():
        total_estaciones = len(lista_estaciones)
        
        for i in range(total_estaciones - 1):
            est_a, tiempo_viaje, _ = lista_estaciones[i]
            est_b, _, _ = lista_estaciones[i+1]
            
            # Definimos los nodos incluyendo la línea para no confundir transferencias
            nodo_a = (est_a, nombre_linea)
            nodo_b = (est_b, nombre_linea)
            
            if nodo_a not in grafo: grafo[nodo_a] = []
            if nodo_b not in grafo: grafo[nodo_b] = []
            
            # Conexión simétrica: El tiempo 'tiempo_viaje' es el mismo de ida y de vuelta
            grafo[nodo_a].append((nodo_b, tiempo_viaje, "VIAJE"))
            grafo[nodo_b].append((nodo_a, tiempo_viaje, "VIAJE"))

    # 3. Conectar las transferencias físicas entre líneas (Costo fijo: 5 minutos)
    for nombre_linea, lista_estaciones in lineas_separadas.items():
        for nombre_est, _, info in lista_estaciones:
            nodo_origen_transf = (nombre_est, nombre_linea)
            
            # Revisamos si tiene transferencias declaradas (elementos a partir del índice 1)
            for elemento in info[1:]:
                if isinstance(elemento, tuple):
                    nombre_destino_transf = elemento[0]
                    info_destino = elemento[2]
                    linea_destino_transf = info_destino[0]
                    
                    nodo_destino_transf = (nombre_destino_transf, linea_destino_transf)
                    
                    if nodo_origen_transf in grafo and nodo_destino_transf in grafo:
                        # Añadimos la transferencia de 5 minutos fijos en ambas direcciones
                        grafo[nodo_origen_transf].append((nodo_destino_transf, 5, "TRANSFERENCIA"))
                        grafo[nodo_destino_transf].append((nodo_origen_transf, 5, "TRANSFERENCIA"))

    return grafo


def calcular_ruta_optima(nombre_origen, nombre_destino, grafo):
    """
    Encuentra la ruta óptima basada en el menor número de estaciones.
    Rastrea el tipo de conexión usado para detectar transferencias de nombres diferentes.
    """
    nodos_origen = [nodo for nodo in grafo if nodo[0] == nombre_origen]
    nodos_destino = [nodo for nodo in grafo if nodo[0] == nombre_destino]
    
    if not nodos_origen or not nodos_destino:
        return None

    # COLA para BFS: (nodo_actual, [(nodo, tipo_conexion)], tiempo_acumulado)
    cola = []
    visitados = set()
    
    for nodo_ini in nodos_origen:
        cola.append((nodo_ini, [(nodo_ini, "INICIO")], 0))
        visitados.add(nodo_ini)
        
    while cola:
        nodo_actual, camino, tiempo_total = cola.pop(0)
        
        # Si el nombre de la estación actual coincide con el destino final, terminamos
        if nodo_actual[0] == nombre_destino:
            return procesar_resultado(camino, tiempo_total)
            
        for vecino, tiempo_tramo, tipo_conexion in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [(vecino, tipo_conexion)], tiempo_total + tiempo_tramo))
                
    return None


def procesar_resultado(camino, tiempo_total):
    """
    Procesa el camino recorrido. Guarda la línea vieja y la nueva 
    cuando detecta un punto de transferencia física.
    """
    estaciones_recorridas = []
    transferencias_realizadas = []
    
    # 1. Extraemos de forma segura el nodo inicial (nombre y su línea base)
    nodo_inicial = camino[0][0]
    nombre_ini, linea_ini = nodo_inicial
    estaciones_recorridas.append(nombre_ini)
    
    # 2. Recorremos el camino desde el segundo paso
    for i in range(1, len(camino)):
        nodo_actual, tipo_conexion = camino[i]
        nodo_anterior, _ = camino[i-1]
        
        nombre_act, linea_act = nodo_actual
        nombre_ant, linea_ant = nodo_anterior
        
        # SI ES UNA TRANSFERENCIA: Capturamos ambas líneas usando los nombres limpios
        if tipo_conexion == "TRANSFERENCIA":
            estaciones_recorridas.append(f"(Transferencia {linea_act})")
            
            transferencias_realizadas.append({
                "desde_estacion": nombre_ant,
                "linea_anterior": linea_ant,
                "hacia_estacion": nombre_act,
                "linea_nueva": linea_act
            })
            
        # Agregamos el nombre a la secuencia visual si cambiamos de estación física
        if nombre_act != nombre_ant:
            estaciones_recorridas.append(nombre_act)
            
    # Contamos las estaciones reales (excluyendo los textos decorativos de transferencia)
    total_reales = len([e for e in estaciones_recorridas if not e.startswith("(")])

    return {
        "secuencia": estaciones_recorridas,
        "tiempo_total": tiempo_total,
        "total_estaciones": total_reales,
        "transferencias": transferencias_realizadas
    }

def mostrar_reporte_pantalla(origen, destino, res):
    """Muestra todo el reporte bonito con barras separadoras, rutas y tiempos"""
    if res:
        print("=" * 50)
        print(f" 🚇 DETALLE DEL VIAJE: {origen} -> {destino} 🚇")
        print("=" * 50)
        print(f"🗺️  Ruta a seguir: {' -> '.join(res['secuencia'])}")
        print(f"🚉 Número total de estaciones a recorrer: {res['total_estaciones']}")
        print(f"⏱️  Tiempo total estimado de viaje: {res['tiempo_total']} minutes")
        
        if res['transferencias']:
            print("\n🔄 Transferencias a realizar:")
            for t in res['transferencias']:
                print(f"   • En '{t['desde_estacion']}' ({t['linea_anterior']}), camina hacia '{t['hacia_estacion']}' ({t['linea_nueva']})")
        else:
            print("\n🟢 Ruta directa (Sin transferencias).")
        print("=" * 50)
        print("¡Buen viaje! 🚇")
    else:
        print("❌ No se encontró ruta.")

if __name__ == "__main__":
    mapa_metro = construir_grafo(estaciones_metro)
    resultado = calcular_ruta_optima("Propatria", "Zoológico", mapa_metro)
    mostrar_reporte_pantalla("Propatria", "Zoológico", resultado)
