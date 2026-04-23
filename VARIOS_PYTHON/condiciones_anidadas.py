# ejercicio 2: decision multiple con elif
calificacion = float(input("Ingresa tu calificación (entre 1 y 7): "))
if calificacion <1 or calificacion >7:
    print("Error: Calificación debe estar entre 1 y 7.")
else:
     if calificacion == 7.0:
        print("¡Excelente! ")
     elif calificacion >= 6.0:
        print("Muy bien ")
     elif calificacion >= 5.0:
        print("Bien ")
     elif calificacion >= 4.0:
        print("Suficiente ")
     else:
        print("Insuficiente")
