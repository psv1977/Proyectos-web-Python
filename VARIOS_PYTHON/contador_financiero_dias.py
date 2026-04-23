#este codigo es para obtener la fecha el pago de deberes tantos dias hacia la fecha actual
# (ya sea para atras en negativo o para adelante en positivo. ).
# el codigo debe entregar el día de la semana que correspone a la fecha futura, y el formato de la fecha debe ser dd/mm/yyyy
# el cogigo debe validar que el numero de dias ingresado sea un numero entero, y en caso de no serlo, debe mostrar un mensaje de error y pedir nuevamente el ingreso del numero de dias.
# el codigo debe validar que el numero de dias ingresado si es un numero negativo, y mostar fecha pasada, y si es un numero positivo, mostrar fecha futura.
from datetime import datetime, timedelta

fecha_actual = datetime.now()
while True:
    try:
        dias = int(input("Ingrese la cantidad de días: "))
        break
    except ValueError:
        print("Error: Por favor, ingrese un número entero.")
        continue        
fecha_futura = fecha_actual + timedelta(days=dias)
print(f"La fecha futura es: {fecha_futura}")
print(f"El día de la semana es: {fecha_futura.strftime('%A')}")
print(f"El formato de la fecha es: {fecha_futura.strftime('%d/%m/%Y')}")


from datetime import datetime, timedelta

DIAS_SEMANA = [
    "lunes",
    "martes",
    "miércoles",
    "jueves",
    "viernes",
    "sábado",
    "domingo",
]


def pedir_dias():
    """Solicita al usuario una cantidad de días y valida que sea un entero."""
    while True:
        try:
            return int(input("Ingrese la cantidad de días: "))
        except ValueError:
            print("Error: por favor, ingrese un número entero.")


def obtener_tipo_fecha(dias):
    """Determina si la fecha calculada es futura, pasada o actual."""
    if dias > 0:
        return "futura"
    if dias < 0:
        return "pasada"
    return "actual"


def main():
    """Calcula una fecha desplazada desde hoy y muestra su día de la semana."""
    fecha_actual = datetime.now()
    dias = pedir_dias()

    fecha_calculada = fecha_actual + timedelta(days=dias)
    tipo_fecha = obtener_tipo_fecha(dias)
    dia_semana = DIAS_SEMANA[fecha_calculada.weekday()]
    fecha_formateada = fecha_calculada.strftime("%d/%m/%Y")

    if tipo_fecha == "actual":
        print(f"La fecha corresponde al día actual: {fecha_formateada}")
    else:
        print(f"La fecha {tipo_fecha} es: {fecha_formateada}")

    print(f"El día de la semana es: {dia_semana}")


if __name__ == "__main__":
    main()



