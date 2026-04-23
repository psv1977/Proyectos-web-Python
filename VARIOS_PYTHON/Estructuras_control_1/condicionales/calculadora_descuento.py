# este ejemplo de codigo construye una calculadora de descuento, dependiendo del monto total de la compra, se aplicará un descuento diferente
monto_compra = float(input("Ingrese el monto total de su compra: $"))
if monto_compra < 100:
    descuento = 0
elif monto_compra < 500:
    descuento = 0.1
else:
    descuento = 0.2
monto_descuento = monto_compra * descuento
print(f"El monto del descuento es: ${monto_descuento:.2f}")
print(f"El monto a pagar es: ${monto_compra - monto_descuento:.2f}")
