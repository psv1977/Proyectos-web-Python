# este codifo construye una calculadora de IVA diferenciado, dependiendo del tipo de producto, se aplicará un IVA diferente
# se definiran un set de productos alimenticios, electrónicos y otros, para validar el tipo de producto ingresado
# el precio final debe mostrarse como numero entero, en pesos chilenos, sin decimales ni simbolo de pesos, solo el numero
# se debe generar una lista de productos con su respectivo IVA, para mostrar al usuario al final del programa, con el formato: "Producto: [nombre], Precio sin IVA: $[precio], IVA: $[monto_iva], Precio final: $[precio_final]"    

import pandas as pd
import os

# TRUCO: Forzamos a Python a situarse en la carpeta donde está este script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Ahora el nombre simple debería funcionar
nombre_archivo = 'productos.csv'

try:
    df = pd.read_csv(nombre_archivo)
    print("✅ Archivo cargado correctamente.")
except Exception as e:
    print(f"❌ Sigue sin encontrarse el archivo. Error: {e}")
    # Si falla, te mostraré dónde está mirando Python exactamente:
    print(f"Buscando en: {os.getcwd()}")
    exit()

# 2. Definir las tasas de IVA por categoría
tasas_iva = {
    "alimenticio": 0.02,
    "electrónico": 0.19,
    "nocivo": 0.30,
    "otro": 0.12
}

# 3. Preparar la "memoria" (carrito de compras)
carrito = []

print("=== SISTEMA DE VENTAS - CHILE ===")
print("Escriba el nombre del producto para agregarlo.")
print("Escriba 'TOTAL' para finalizar y ver el detalle.\n")

# 4. Bucle principal (Interacción)
while True:
    seleccion = input("Producto a comprar: ").lower().strip()
    
    if seleccion == "total":
        break
    
    # Buscar el producto en el DataFrame
    if seleccion in df['Producto'].values:
        # Extraer los datos de la fila correspondiente
        datos_prod = df[df['Producto'] == seleccion].iloc[0]
        
        # Obtener valores individuales
        nombre = datos_prod['Producto']
        precio_base = datos_prod['Precio']
        categoria = datos_prod['Categoria']
        
        # Calcular el IVA según la categoría
        tasa = tasas_iva.get(categoria, 0.19) # 0.19 por defecto si no encuentra categoría
        monto_iva = int(round(precio_base * tasa))
        precio_final = precio_base + monto_iva
        
        # Guardar en el carrito como un diccionario
        item = {
            "nombre": nombre.capitalize(),
            "precio_base": precio_base,
            "iva": monto_iva,
            "total": precio_final
        }
        carrito.append(item)
        print(f" > {nombre.capitalize()} agregado: ${precio_final}")
    else:
        print(f" x El producto '{seleccion}' no existe en la lista. Intente de nuevo.")

# 5. Mostrar resultados finales
if len(carrito) > 0:
    print("\n" + "="*60)
    print("RESUMEN DE COMPRA")
    print("="*60)
    
    total_boleta = 0
    for prod in carrito:
        print(f"Producto: [{prod['nombre']}], Precio sin IVA: ${prod['precio_base']}, IVA: ${prod['iva']}, Precio final: ${prod['total']}")
        total_boleta += prod['total']
    
    print("-" * 60)
    print(f"TOTAL A PAGAR: ${total_boleta}")
    print("="*60)
else:
    print("\nNo se realizaron compras.")