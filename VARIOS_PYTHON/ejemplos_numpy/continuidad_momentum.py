import math

# radio del tubo pequeño (pies)
r_s = 0.5

# caudal Q calculado analíticamente
Q = 2 * math.pi * (3.125 * r_s**2 - r_s**4 / 4)

# área del tubo pequeño
A = math.pi * r_s**2

# velocidad promedio
v_prom = Q / A

print(f"Velocidad promedio = {v_prom:.3f} pies/s")





import math

R = 2.5  # radio del tanque
A_B = math.pi / 4  # area del tubo pequeño

Q_in = 2 * math.pi * (3.125 * R**2 - R**4 / 4)
V_B = Q_in / A_B

print(f"Velocidad promedio en el tubo pequeño = {V_B:.3f} pies/s")



import numpy as np

# ----------------------------
# DATOS (ejemplo simbólico)
# ----------------------------
rho = 1000          # kg/m^3
A1 = 0.02           # m^2
A2 = 0.01           # m^2
V1 = 5.0            # m/s
V2 = 10.0           # m/s
p1 = 200_000        # Pa
p2 = 100_000        # Pa
theta = np.deg2rad(30)  # rad
W = 100.0           # N (peso del fluido)

# ----------------------------
# GASTO MÁSICO
# ----------------------------
mdot = rho * A1 * V1

# ----------------------------
# VELOCIDADES
# ----------------------------
V1_vec = np.array([V1, 0])
V2_vec = np.array([V2*np.cos(theta), V2*np.sin(theta)])

# ----------------------------
# FUERZAS DE PRESIÓN
# ----------------------------
Fp1 = np.array([p1 * A1, 0])
Fp2 = np.array([-p2 * A2 * np.cos(theta),
                -p2 * A2 * np.sin(theta)])

# ----------------------------
# ECUACIÓN DE MOMENTUM
# ----------------------------
R = mdot * (V2_vec - V1_vec) - Fp1 - Fp2 + np.array([0, W])

Rx, Ry = R

print(f"Rx = {Rx:.2f} N")
print(f"Ry = {Ry:.2f} N")