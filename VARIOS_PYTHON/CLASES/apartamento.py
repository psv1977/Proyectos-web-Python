class Apartamento:
    def __init__(self, metros, orientacion, precio, estado, numero , piso, habitaciones):
        self.metros = metros
        self.orientacion = orientacion
        self.precio = precio
        self.estado = estado
        self.numero = numero
        self.piso = piso
        self.habitaciones = habitaciones

    def mostrar_info(self):
        return f"Apartamento {self.numero} en el piso {self.piso} con {self.habitaciones} habitaciones."
    
apartamento1 = Apartamento(80, "Norte", 150000, "Disponible", 101, 1, 3)
apartamento2 = Apartamento(60, "Sur", 120000, "Vendido", 202, 2, 2)
apartamento3 = Apartamento(90, "Este", 180000, "Disponible", 303, 3, 4)
apartamento4 = Apartamento(70, "Oeste", 130000, "Vendido", 404, 4, 2)
apartamento5 = Apartamento(100, "Norte", 200000, "Disponible", 505, 5, 5)
print(apartamento1.mostrar_info())
print(apartamento2.mostrar_info())
print(apartamento3.mostrar_info())
print(apartamento4.mostrar_info())
print(apartamento5.mostrar_info())