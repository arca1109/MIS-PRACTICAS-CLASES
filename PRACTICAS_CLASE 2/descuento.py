print("Hola, bienvenido! Verifica tu descuento")
precio = float(input("Introduce el precio del producto: "))
porcentaje_descuento = float(input("Introduce el porcentaje de descuento: "))

monto_descuento = precio * (porcentaje_descuento / 100)
precio_final = precio - monto_descuento

print(f"El precio final del producto con el {porcentaje_descuento}% de descuen to es: {precio_final:.2f}")
