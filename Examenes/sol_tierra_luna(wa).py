
import numpy as np
import matplotlib.pyplot as plt
# Constantes
G = 6.674e-11
m1 = 5.97e24 # Masa de la Tierra
m2 = 7.342e22 # Masa de la Luna
m3 = 1.989e30 # Masa del Sol
r0 = 1.495978707e11 # Distancia Tierra-Sol inicial
v0 = 2.9783e4 # Velocidad de la Tierra

# Condiciones iniciales
x1 = r0 # Posición inicial de la Tierra en el eje x
y1 = 0 # Posición inicial de la Tierra en el eje y
x2 = r0 + 3.844e8 # Posición inicial de la Luna en el eje x
y2 = 0 # Posición inicial de la Luna en el eje y
vx1 = 0 # Velocidad inicial de la Tierra en el eje x
vy1 = v0 # Velocidad inicial de la Tierra en el eje y
vx2 = 0 # Velocidad inicial de la Luna en el eje x
vy2 = v0 + 1022 # Velocidad inicial de la Luna en el eje y

# Tiempo
t = 0
dt = 60*60*24 # 1 día

# Listas para guardar los valores de la posición de la Tierra y la Luna
x1_list = []
y1_list = []
x2_list = []
y2_list = []

# Ciclo para calcular la posición de la Tierra y la Luna en cada instante de tiempo
while t <= 365*24*60*60: # 1 año
    # Distancias entre la Tierra y la Luna
    r12 = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    r13 = np.sqrt(x1**2 + y1**2)
    r23 = np.sqrt(x2**2 + y2**2)

    ax1 = -G*m3*x1/r13**3 - G*m2*(x1-x2)/r12**3
    ay1 = -G*m3*y1/r13**3 - G*m2*(y1-y2)/r12**3
    ax2 = -G*m3*x2/r23**3 - G*m1*(x2-x1)/r12**3
    ay2 = -G*m3*y2/r23**3 - G*m1*(y2-y1)/r12**3

    # Nuevas velocidades de la Tierra y la Luna
    vx1 += ax1*dt
    vy1 += ay1*dt
    vx2 += ax2*dt
    vy2 += ay2*dt

    # Nuevas posiciones de la Tierra y la Luna
    x1 += vx1*dt
    y1 += vy1*dt
    x2 += vx2*dt
    y2 += vy2*dt

    # Agregar las posiciones a las listas
    x1_list.append(x1)
    y1_list.append(y1)
    x2_list.append(x2)
    y2_list.append(y2)

    # Actualizar el tiempo
    t += dt

plt.figure(figsize=(8,8)) # Aumentar tamaño de la figura
plt.xlim([-2*r0, 2*r0]) # Limitar los valores del eje x para acercar la imagen
plt.ylim([-2*r0, 2*r0]) # Limitar los valores del eje y para acercar la imagen
plt.plot(x1_list, y1_list, label='Tierra')
plt.plot(x2_list, y2_list, label='Luna')
plt.plot(0, 0, 'ro', markersize=10, label='Sol')
plt.legend()
plt.show()
