# este codigo es para que cuando se ingresa un año, el programa determine si es bisiesto o no a través de una funcion   

año = int(input("Ingrese un año: "))

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False        

if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")          