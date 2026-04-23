# Este código realiza varios calculos relacionados con la vibración torsional de un sistema mecánico utilizando NumPy.
# Es un sistema torsional de 1GDL, donde se quiere entender la fisica : inercia, riogideZ, amortiguamiento y torque excitador, y se resuelve la ecuacion diferencial de segundo orden que describe el movimiento torsional, utilizando el metodo de Euler para obtener la respuesta del sistema a lo largo del tiempo.
# Se grafican los resultados para visualizar la vibración torsional del sistema.
# El objetivo es el uso de iteraciones para la obtención de los resultados, y el uso de condiciones para entender la fisica del sistema. 
# Ademas se busca comparar los resultados obtenidos con espectros medidos para validar el modelo.

import numpy as np
import matplotlib.pyplot as plt     

# Parámetros del sistema
momento_de_inercia = 0.15     # Momento de inercia
rigidez_torsional = 1200     # Rigidez torsional
amortiguamento_torsional = 0.08  # Amortiguamiento torsional
torque_excitador = 20          # Torque excitador
frecuencia_excitadora = 12      # Frecuencia del torque excitador (Hz)
frecuencia_angular_excitadora = 2 * np.pi * frecuencia_excitadora  # Frecuencia angular del torque excitador

# Función para calcular la aceleración angular
def aceleracion_angular(theta, omega):
    return (-rigidez_torsional * theta - amortiguamento_torsional * omega) / momento_de_inercia

# Simulación de la vibración torsional
t_max = 5  # Tiempo total de simulación
dt = 0.1   # Paso de tiempo
t = np.arange(0, t_max, dt)  # Vector de tiempo
theta = np.zeros_like(t)  # Vector para almacenar el ángulo en cada instante
omega = np.zeros_like(t)  # Vector para almacenar la velocidad angular en cada instante

# Condiciones iniciales
theta_0 = 0.05  # Ángulo inicial
omega_0 = 0     # Velocidad angular inicial
theta[0] = theta_0
omega[0] = omega_0

# Simulación usando el método de Euler
for i in range(1, len(t)):
    # Calculamos el torque excitador en el instante actual
    torque_actual = torque_excitador * np.sin(frecuencia_angular_excitadora * t[i-1])
    
    # Calculamos la aceleración angular considerando el torque excitador
    alpha = aceleracion_angular(theta[i-1], omega[i-1]) + torque_actual / momento_de_inercia
    
    # Actualizamos la velocidad angular y el ángulo usando el método de Euler
    omega[i] = omega[i-1] + alpha * dt
    theta[i] = theta[i-1] + omega[i] * dt

# Determinacio de las frecuencias naturales del sistema
frecuencia_natural = np.sqrt(rigidez_torsional / momento_de_inercia) / (2 * np.pi)
print(f"Frecuencia natural del sistema: {frecuencia_natural:.2f} Hz")   

# Integracion temporal para obtener la respuesta libre del sistema (sin torque excitador)
theta_libre = np.zeros_like(t)
omega_libre = np.zeros_like(t)
theta_libre[0] = theta_0
omega_libre[0] = omega_0


# Graficar los resultados
plt.figure(figsize=(10, 5))
plt.plot(t, theta, label='Ángulo')
plt.title('Vibración Torsional con Torque Excitador')
plt.xlabel('Tiempo (s)')
plt.ylabel('Ángulo (rad)')
plt.legend()
plt.grid(True)
plt.show()  
