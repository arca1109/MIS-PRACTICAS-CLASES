import random

estaciones_metro = [
    # --- LÍNEA 1 ---
    ("Propatria", random.randint(1, 5), ["Línea 1"]),
    ("Pérez Bonalde", random.randint(1, 5), ["Línea 1"]),
    ("Plaza Sucre", random.randint(1, 5), ["Línea 1"]),
    ("Gato Negro", random.randint(1, 5), ["Línea 1"]),
    ("Agua Salud", random.randint(1, 5), ["Línea 1"]),
    ("Caño Amarillo", random.randint(1, 5), ["Línea 1"]),
    ("Capitolio", random.randint(1, 5), ["Línea 1", ("El Silencio", 5, ["Línea 2"])]), # Transferencia a L2 (El Silencio)
    ("La Hoyada", random.randint(1, 5), ["Línea 1"]),
    ("Parque Carabobo", random.randint(1, 5), ["Línea 1"]),
    ("Bellas Artes", random.randint(1, 5), ["Línea 1"]),
    ("Colegio de Ingenieros", random.randint(1, 5), ["Línea 1"]),
    ("Plaza Venezuela", random.randint(1, 5), 
    ["Línea 1", ("Plaza Venezuela 2", 4, ["Línea 3"]), ("Zona Rental", 6, ["Línea 4"])]),  # Transferencia a L3 y L4 (Zona Rental)
    ("Sabana Grande", random.randint(1, 5), ["Línea 1"]),
    ("Chacaíto", random.randint(1, 5), ["Línea 1"]),
    ("Chacao", random.randint(1, 5), ["Línea 1"]),
    ("Altamira", random.randint(1, 5), ["Línea 1"]),
    ("Miranda", random.randint(1, 5), ["Línea 1"]),
    ("Los Dos Caminos", random.randint(1, 5), ["Línea 1"]),
    ("Los Cortijos", random.randint(1, 5), ["Línea 1"]),
    ("La California", random.randint(1, 5), ["Línea 1"]),
    ("Petare", random.randint(1, 5), ["Línea 1"]),
    ("Palo Verde", random.randint(1, 5), ["Línea 1"]),

    # --- LÍNEA 2 ---
    ("El Silencio", random.randint(1, 5), ["Línea 2", ("Capitolio", 5, ["Línea 1"])]),  # Transferencia a L1 (Capitolio)
    ("Capuchinos", random.randint(1, 5), ["Línea 2", ("Capuchinos", 2, ["Línea 4"])]),  # Transferencia a L4
    ("Maternidad", random.randint(1, 5), ["Línea 2"]),
    ("Artigas", random.randint(1, 5), ["Línea 2"]),
    ("La Yaguara", random.randint(1, 5), ["Línea 2"]),
    ("Carapita", random.randint(1, 5), ["Línea 2"]),
    ("Antímano", random.randint(1, 5), ["Línea 2"]),
    ("Mamera", random.randint(1, 5), ["Línea 2"]),
    ("Caricuao", random.randint(1, 5), ["Línea 2"]),
    ("Zoológico", random.randint(1, 5), ["Línea 2"]),
    ("Ruiz Pineda", random.randint(1, 5), ["Línea 2"]),
    ("Las Adjuntas", random.randint(1, 5), ["Línea 2"]),

    # --- LÍNEA 3 ---
    ("Plaza Venezuela 2", random.randint(1, 5), ["Línea 3", ("Plaza Venezuela", 4, ["Línea 1"]), ("Zona Rental", 6, ["Línea 4"])]),  # Transferencia a L1 y L4 (Zona Rental)
    ("Ciudad Universitaria", random.randint(1, 5), ["Línea 3"]),
    ("Los Símbolos", random.randint(1, 5), ["Línea 3"]),
    ("La Bandera", random.randint(1, 5), ["Línea 3"]),
    ("El Valle", random.randint(1, 5), ["Línea 3"]),
    ("Los Jardines", random.randint(1, 5), ["Línea 3"]),
    ("Coche", random.randint(1, 5), ["Línea 3"]),
    ("Mercado", random.randint(1, 5), ["Línea 3"]),
    ("La Rinconada", random.randint(1, 5), ["Línea 3"]),

    # --- LÍNEA 4 ---
    ("Zona Rental", random.randint(1, 5), # Transferencia a L1, L3 (Plaza Venezuela 2) y L5 (Bello Monte) 
    ["Línea 4", ("Plaza Venezuela", 6, ["Línea 1"]), ("Plaza Venezuela 2", 6, ["Línea 3"]), ("Bello Monte", 3, ["Línea 5"])]),  
    ("Parque Central", random.randint(1, 5), ["Línea 4"]),
    ("Nuevo Circo", random.randint(1, 5), ["Línea 4"]),
    ("Teatros", random.randint(1, 5), ["Línea 4"]),
    ("Capuchinos", random.randint(1, 5), ["Línea 4", ("Capuchinos", 2, ["Línea 2"])]),  # Transferencia a L2

    # --- LÍNEA 5 ---
    ("Bello Monte", random.randint(1, 5), ["Línea 5", ("Zona Rental", 3, ["Línea 4"])]),  # Transferencia a L4 (Zona Rental)
]