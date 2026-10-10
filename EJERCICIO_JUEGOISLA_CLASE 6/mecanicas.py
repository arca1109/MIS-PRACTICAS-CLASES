import pandas as pd

def procesar_cambios_escena(escena, estado_jugador):
    """Actualiza la salud, hambre y día basándose en los datos de la escena."""
    # Modificar salud
    cambio_salud = escena.get('cambio_salud')
    if pd.notna(cambio_salud):
        estado_jugador['salud'] += int(cambio_salud)
        # Limitar la salud entre 0 y 100
        estado_jugador['salud'] = max(0, min(100, estado_jugador['salud']))

    # Modificar hambre
    cambio_hambre = escena.get('cambio_hambre')
    if pd.notna(cambio_hambre):
        estado_jugador['hambre'] += int(cambio_hambre)
        estado_jugador['hambre'] = max(0, min(100, estado_jugador['hambre']))

    # Avanzar un día al cambiar de escena principal
    estado_jugador['dia'] += 1

def agregar_objeto(inventario, escena):
    """Añade un objeto al inventario si la escena lo otorga y no lo tiene."""
    objeto = escena.get('otorga_objeto')
    if pd.notna(objeto) and str(objeto).strip() != "":
        if objeto not in inventario:
            inventario.append(objeto)
            print(f"\n✨ ¡Has conseguido un nuevo objeto: {objeto}!")

def validar_requesito(escena, inventario, opcion_letra):
    """Valida si el jugador cumple con el requisito de objeto para la opción elegida."""
    req = escena.get('requiere_objeto')
    if pd.isna(req) or str(req).strip() == "":
        return True
    
    # Si requiere un objeto, verificamos que esté en el inventario
    if req in inventario:
        return True
    return False