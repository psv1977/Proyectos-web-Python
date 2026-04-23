#en este ejemplo vamos a simular la vibracion torsional de un eje, utilizando la ecuacion diferencial de segundo orden 
# que describe el movimiento torsional, y resolviendola numericamente con el metodo de Euler.
#adicionalmente se resolveran para obtener los siguientes resultasdos:
# sistema de 1 grado de libertad
# sistema de 2 o más inercias torsionales
# análisis modal
#frecuencias naturales
#respuesta libre y forzada
#amortiguamiento
#torque periódico
#excitación armónica
#comparación con espectros medidos


import numpy as np
import matplotlib.pyplot as plt     


# Parámetros del sistema
momento_de_inercia = 0.02     # Momento de inercia
rigidez_torsional = 1.0     # Rigidez torsional
amortiguamento_torsional = 0.02  # Amortiguamiento torsional

# Función para calcular la aceleración angular
def aceleracion_angular(theta, omega):
    return (-rigidez_torsional * theta - amortiguamento_torsional * omega) / momento_de_inercia 


# Simulación de la vibración torsional
t_max = 10  # Tiempo total de simulación
dt = 0.01   # Paso de tiempo
t = np.arange(0, t_max, dt)  # Vector de tiempo
theta = np.zeros_like(t)  # Vector para almacenar el ángulo en cada instante
omega = np.zeros_like(t)  # Vector para almacenar la velocidad angular en cada instante

# Condiciones iniciales
theta_0 = 0.1  # Ángulo inicial
omega_0 = 0    # Velocidad angular inicial
theta[0] = theta_0
omega[0] = omega_0

# Simulación usando el método de Euler

for i in range(1, len(t)):
    alpha = aceleracion_angular(theta[i-1], omega[i-1])  # Aceleración angular en el instante anterior
    omega[i] = omega[i-1] + alpha * dt        # Actualizar velocidad angular
    theta[i] = theta[i-1] + omega[i] * dt     # Actualizar ángulo

# Graficar los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, theta, label='Ángulo')
plt.title('Vibración Torsional')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.legend()
plt.grid(True)
plt.show()  
