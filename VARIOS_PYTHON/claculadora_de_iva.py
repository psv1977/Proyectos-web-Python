#este codigo se encarga de calcular el IVA del 19% a los productos que se venden

def calcular_iva(precio):
    iva = precio * 0.19
    return iva  #retorna el valor del IVA calculado
#ejemplo de uso
precio_producto = 210000
  #precio del producto sin IVA
iva_producto = calcular_iva(precio_producto)  #calcula el IVA del producto
print(f"El IVA del producto es: {iva_producto:.3f}")  #imprime el IVA con dos decimales 
precio_total = precio_producto + iva_producto
print(f"El precio total del producto con IVA es: {precio_total}")
