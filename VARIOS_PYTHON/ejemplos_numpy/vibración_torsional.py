# Este ejemplo en Python muestra cómo usar NumPy para simular la vibración torsional de un sistema mecánico.    
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
momento_de_inercia = 0.01  # Momento de inercia (kg*m^2)
rigidez_torsional = 0.1   # Rigidez torsional (N*m/rad)

# Función para calcular la aceleración angular
def aceleracion_angular(theta):
    return -rigidez_torsional / momento_de_inercia * theta   

# Simulaci60ón de la vibración torsional
t_max = 5 # Tiempo total de simulación (s)
dt = 0.1    # Paso de tiempo (s)  
t = np.arange(0, t_max, dt)  # Vector de tiempo
theta = np.zeros_like(t)  # Vector para almacenar el ángulo en cada instante    
omega = np.zeros_like(t)  # Vector para almacenar la velocidad angular en cada instante


# Condiciones iniciales
theta_0 = 0.1  # Ángulo inicial (rad)
omega_0 = 0    # Velocidad angular inicial (rad/s)
theta[0] = theta_0
omega[0] = omega_0

# Simulación usando el método de Euler
for i in range(1, len(t)):
    alpha = aceleracion_angular(theta[i-1])  # Aceleración angular en el instante anterior
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



