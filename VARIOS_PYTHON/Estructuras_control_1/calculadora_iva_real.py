import pandas as pd
import os

# 1. Asegurar que Python mire en la carpeta correcta
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except:
    pass # Si falla (ej. en consola interactiva), continúa

nombre_archivo = 'productos.csv'

# 2. Cargar base de datos
try:
    df = pd.read_csv(nombre_archivo)
    print("✅ Base de datos cargada. Precios detectados como 'IVA INCLUIDO'.")
except Exception as e:
    print(f"❌ Error al cargar el archivo: {e}")
    exit()

tasas_iva = {
    "alimenticio": 0.02,
    "electrónico": 0.19,
    "nocivo": 0.30,
    "otro": 0.12
}

carrito = []

print("\n=== SISTEMA DE VENTAS (MODO DESGLOSE IVA) ===")
print("Escriba 'TOTAL' para finalizar.\n")

while True:
    seleccion = input("Producto a comprar: ").lower().strip()
    
    if seleccion == "total":
        break
    
    if seleccion in df['Producto'].values:
        datos_prod = df[df['Producto'] == seleccion].iloc[0]
        
        # VALORES ORIGINALES (Desde el Excel)
        precio_bruto = datos_prod['Precio'] # Este ya incluye IVA
        categoria = datos_prod['Categoria']
        tasa = tasas_iva.get(categoria, 0.19)
        
        # --- NUEVOS CÁLCULOS DE DESGLOSE ---
        # 1. Obtenemos el precio neto (sin IVA)
        precio_neto = int(round(precio_bruto / (1 + tasa)))
        # 2. El IVA es la diferencia
        monto_iva = precio_bruto - precio_neto
        
        item = {
            "nombre": datos_prod['Producto'].capitalize(),
            "precio_sin_iva": precio_neto,
            "monto_iva": monto_iva,
            "precio_final": precio_bruto
        }
        carrito.append(item)
        print(f" > {item['nombre']} agregado (Total: ${precio_bruto})")
    else:
        print(f" x No existe '{seleccion}' en la lista.")

# 5. Reporte Final
if carrito:
    print("\n" + "="*70)
    print("DETALLE DE LA BOLETA (Precios en CLP)")
    print("="*70)
    
    suma_total = 0
    for p in carrito:
        # Formato solicitado por Andrea
        print(f"Producto: [{p['nombre']}], Precio sin IVA: ${p['precio_sin_iva']}, IVA: ${p['monto_iva']}, Precio final: ${p['precio_final']}")
        suma_total += p['precio_final']
    
    print("-" * 70)
    print(f"TOTAL A PAGAR: ${suma_total}")
    print("="*70)