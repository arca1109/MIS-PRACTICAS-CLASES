Base_de_datos = [
    ("Tyrannosaurus Rex", "Rex", "Carnívoro", "Cretácico Superior"),
    ("Triceratops", "Triceratops", "Herbívoro", "Cretácico Superior"),
    ("Velociraptor", "Velociraptor", "Carnívoro", "Cretácico Superior"),
    ("Arqueopterix", "Archaeopteryx", "Carnívoro", "Jurásico Superior"),
    ("Stegosaurus", "Stegosaurus", "Herbívoro", "Jurásico Superior"),
    ("Brachiosaurus", "Brachiosaurus", "Herbívoro", "Jurásico Superior"),
]

# Diccionario para mapear la opción del menú con el índice de la tupla y su nombre
MAPEO_OPCIONES = {
    "1": {"indice": 0, "nombre": "🦕 Nombre"},
    "2": {"indice": 1, "nombre": "🦖 Tipo"},
    "3": {"indice": 2, "nombre": "🥗 Dieta"},
    "4": {"indice": 3, "nombre": "🕑 Periodo"}
}

def mostrar_dinosaurio(dino):
    """Muestra toda la información de un dinosaurio."""
    print(f"🦕 Nombre: {dino[0]} | Tipo: {dino[1]} | Dieta: {dino[2]} | Periodo: {dino[3]}")

print("Bienvenido a la base de datos de dinosaurios.")
print("Aquí puedes buscar información sobre diferentes dinosaurios según su nombre, tipo, dieta o periodo.")

while True: #Bucle principal del programa
    print("\n 🗒️  MENÚ PRINCIPAL: ¿Cómo deseas buscar la información?")
    print("1. Por Nombre")
    print("2. Por Tipo")
    print("3. Por Dieta")
    print("4. Por Periodo")
    print("5. Salir")
    
    opcion_principal = input("Elija una opción (1-5): ").strip()
    
    if opcion_principal == "5":
        print("¡Gracias por usar la base de datos de dinosaurios!🦕 Hasta luego.🖐️")
        print("¡Saliendo del programa!")
        break
        
    if opcion_principal in MAPEO_OPCIONES:
        campo_info = MAPEO_OPCIONES[opcion_principal]
        indice_tupla = campo_info["indice"]
        nombre_campo = campo_info["nombre"]
        
        # Segundo menú: Tipo de búsqueda
        print(f"\n🗒️  BÚSQUEDA POR {nombre_campo.upper()} ---")
        print("1. Búsqueda específica (Acepta texto parcial)")
        print("2. Búsqueda general (Ver todos los elementos disponibles)")
        
        tipo_busqueda = input("Elija el tipo de búsqueda (1-2): ").strip()
        
        if tipo_busqueda == "1":
            # Búsqueda Específica / Sugerencias
            valor_buscar = input(f"Introduce el {nombre_campo} (o parte de él): ").strip().lower()
            
            if not valor_buscar:
                print("❌ No ingresaste ningún texto para buscar.")
                continue
                
            coincidencias = []
            
            # Buscamos si el texto ingresado está CONTENIDO en el dato de la tupla
            for dino in Base_de_datos:
                if valor_buscar in dino[indice_tupla].lower():
                    coincidencias.append(dino)
            
            # Mostramos los resultados obtenidos
            if coincidencias:
                print(f"\n Se encontraron {len(coincidencias)} resultado(s)/sugerencia(s):")
                for coincidencia in coincidencias:
                    mostrar_dinosaurio(coincidencia)
            else:
                print(f"❌ No se encontraron sugerencias ni coincidencias para tu búsqueda.")
                
        elif tipo_busqueda == "2": 
           # Búsqueda General: Muestra una lista sin repetir y la cantidad total
            valores_existentes = set(dino[indice_tupla] for dino in Base_de_datos)
            print(f"\n Hay un total de {len(valores_existentes)} {nombre_campo.lower()}s registrados, que son:  ")
            for valor in sorted(valores_existentes):
                print(f" - {valor}")
                
        else:
            print("❌ Opción de búsqueda no válida.")
            
    else:
        print("❌ Opción del menú principal" " no válida. Por favor, elige entre 1 y 5.")