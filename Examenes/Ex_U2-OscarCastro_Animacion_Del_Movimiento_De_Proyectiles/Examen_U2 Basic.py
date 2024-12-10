"""
Nombre: Examen Unidad 2 OscarCastro Movimiento De Proyectiles Caso Ideal
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button

# Funciones------------------------------

def Grados_A_Radianes(A0):
     return (A0*np.pi)/180

def Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h):
     global i, j, g, xg, yg, tg, vg, v
     
     tf = 100000000
     vx0 = v0*np.cos(Grados_A_Radianes(A0)) # Velocidad inicial en direccion x
     vy0 = v0*np.sin(Grados_A_Radianes(A0)) # Velocidad inicial en direccion y
     v = np.sqrt(vx0**2+vy0**2)
     xg = [x0]   # Lista para guardar las interaciones de x(t)
     yg = [y0]   # Lista para guardar las interaciones de y(t)
     tg = [t0]   # Lista para guardar las interaciones del tiempo
     vg = [v]
     
     while t0 < tf: # Metodo de Euler
          vx0 = vx0
          x0 = x0 + vx0*h
          vy0 = vy0 - g*h
          y0 = y0 + vy0*h
          t0 += h
          v = np.sqrt(vx0**2+vy0**2)
          xg.append(x0)
          yg.append(y0)
          tg.append(t0)
          vg.append(v)

          if y0 < 0: # Criterio de paro cuando el proyectil cae
               tf = t0
     
#Variables------------------------------

x0 = 0    # Posicion inicial
y0 = 0    # Altura inicial
t0 = 0    # Tiempo inicial
tf = 0
g = 9.81  # Aceleracion de la gravedad

# Condiciones Iniciales Modificar Para La Animacion
A0 = 10   # Angulo Inicial
v0 = 700    # Velocidad inicial
h = .001   # Tamaño de paso

N = f"Metodo de Euler\nMovimiento De Proyectiles Caso Ideal\n"
# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.

Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h)

if v0 <= 50:
     dx = v0/100
     dy = v0/50
elif v0 > 50:
     dx = v0/10
     dy = v0/5

plt.style.use("dark_background")
fig, ax = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
def update(i):
     ax.clear()
     ax.set_title(N+fr"$y$ vs $x$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     ax.grid(color = "turquoise")
     ax.axhline(color = "red")
     ax.axvline(color = "red")
     ax.plot(xg[i],yg[i],"o", color = "yellow",
             label = f"Angulo = {A0}°\nv   = {round(vg[i],3)} m/s\nvi = {v0} m/s\nt  = {round(tg[i],3)} s\ntf = {round(max(tg),3)} s\nx  = {round(xg[i],3)} m\ny  = {round(yg[i],3)} m")
     ax.plot(xg[:i],yg[:i],"--", color = "yellow", lw = .5, ms = 1)
     ax.set_xlim(min(xg)-dx,max(xg)+dx)
     ax.set_ylim(min(yg)-dy,max(yg)+dy)
     ax.legend(edgecolor = "red", fontsize = 15, labelcolor = "yellow")
     
ani = animation.FuncAnimation(fig,update,range(0,len(xg),v0*5), interval = 0)

plt.show()
     