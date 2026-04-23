# el clasificador de edades
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad no válida")
elif edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")   
    