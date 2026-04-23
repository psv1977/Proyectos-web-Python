#este codigo debe mostrar el flujo de autenticacion de un usuario, solicitando su nombre de usuario (email) y contraseña 
# (debe tener menos de 8 caracteres y maximo 12 caracteres con una letra mayuscula, una letra minuscula y un numero o simbolo),
#  y validando si las credenciales son correctas o no. El programa debe permitir hasta 
#3 intentos para ingresar las credenciales correctas, y mostrar un mensaje de error si se superan los intentos permitidos. 
# se debe realizar con condiciones anidadas y con un contador de intentos.

USUARIO_CORRECTO = "admin@example.com"
CONTRASEÑA_CORRECTA = "Password123!"

intentos = 0    

while intentos < 3:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == USUARIO_CORRECTO:
        if contraseña == CONTRASEÑA_CORRECTA:
            print("¡Autenticación exitosa! Bienvenido.")
            break
        else:
            print("Contraseña incorrecta. Intente nuevamente.")
    else:
        print("Nombre de usuario incorrecto. Intente nuevamente.")

    intentos += 1

if intentos == 3:
    print("Se han agotado los intentos. Acceso denegado.")  


