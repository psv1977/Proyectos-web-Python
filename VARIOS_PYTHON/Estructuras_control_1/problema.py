#este codigo determina la fecha, inclyendo el día de la semana, ya sea años ºpara atras o años futuros, teniendo en cuenta los años bisiestos y el calendario gregoriano.
import datetime
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def dias_en_mes(mes, anio):
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif mes in [4, 6, 9, 11]:
        return 30
    elif mes == 2:
        return 29 if es_bisiesto(anio) else 28
    else:
        raise ValueError("Mes no válido")
def calcular_fecha(dia, mes, anio):
    fecha = datetime.date(anio, mes, dia)
    dia_semana = fecha.strftime("%A")
    return fecha, dia_semana
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
anio = int(input("Ingrese el año: "))
fecha, dia_semana = calcular_fecha(dia, mes, anio)
print(f"La fecha es: {fecha}")
print(f"El día de la semana es: {dia_semana}")  

