import pandas as pd
from datetime import datetime

def cargar_escenas(ruta_archivo="escenas_isla.xlsx"):
    """Carga el archivo Excel de escenas en un DataFrame de pandas."""
    try:
        df = pd.read_excel(ruta_archivo)
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{ruta_archivo}'.")
        return None

def buscar_escena(df, id_escena):
    """Busca y devuelve la fila correspondiente a la escena actual como una Serie."""
    fila = df[df["id_escena"] == id_escena]
    if not fila.empty:
        return fila.squeeze()
    return None

def guardar_estado_partida(escena_final, inventario, tipo_final):
    """Guarda el estado final de la partida en un archivo Excel usando pandas."""
    estado = {
        "escena_final": escena_final,
        "inventario": ", ".join(inventario) if inventario else "sin objetos",
        "tipo_final": tipo_final if pd.notna(tipo_final) else "neutral",
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }
    df_estado = pd.DataFrame([estado])
    df_estado.to_excel("estado_partida.xlsx", index=False)
    print("\n📁 Partida guardada exitosamente en 'estado_partida.xlsx'.")