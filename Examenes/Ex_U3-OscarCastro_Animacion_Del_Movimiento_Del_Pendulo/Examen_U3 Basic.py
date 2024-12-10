"""
Nombre: Examen Unidad 3 OscarCastro El Pendulo Simple
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

def Metodo_De_Euler(θ0,w0,t0,tf,h):
     global g, l, m, θg, tg, xg, yg
     θi = Grados_A_Radianes(θ0) 
     θg = [θi] # Lista para guardan las interaciones de θ(t) Euler
     tg = [t0] # Lista para guardar las interaciones del tiempo Euler

     while t0 < tf: # Metodo de Euler
          
          θi = θi + w0*h
          w0 = w0 - (g/l)*θi*h
          t0 += h
          
          θg.append(θi)
          tg.append(t0)

     xg = -l*np.sin(θg)
     yg = -l*np.cos(θg)
#Variables------------------------------

θ0 = 15 # Angulo inicial
w0 = 0                       # Velocidad angular inicial
l = 10                        # Longitud del pendulo
g = 9.81                     # Aceleracion de la gravedad
t0 = 0                       # Tiempo inicial
tf = 10                      # Tiempo final
h = .001                     # Tamaños de paso

N = f"Metodo de Euler vs Metodo de Euler Cromer\nEl Péndulo Simple"
# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(θ0,w0,t0,tf,h)

#if v0 <= 50:
#     dx = v0/100
#     dy = v0/50
#elif v0 > 50:
#     dx = v0/10
#     dy = v0/5

plt.style.use("dark_background")
fig, ax = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
def update(i):
     ax.clear()
     ax.set_title(N+fr"$y$ vs $x$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     #ax.grid(color = "turquoise")
     ax.axhline(color = "red")
     #ax.axvline(color = "red")
     ax.plot([0,xg[i]],[0,yg[i]], color = "red")
     ax.plot(xg[i],yg[i],"o", color = "yellow", label = f"Angulo = {θ0}°\nL   = {l} m\ntf  = {round(max(tg),3)} s\nθ   = {round(θg[i],3)}°\nt    = {round(tg[i],3)} s\nx   = {round(xg[i],3)} m\ny   = {round(yg[i],3)}")
     ax.plot(xg[:i],yg[:i],"--", color = "yellow",lw = .5, ms = 1)
     ax.set_xlim(-l,l)
     ax.set_ylim(-l-l/8,l/8)
     ax.legend(edgecolor = "red", fontsize = 15, labelcolor = "yellow")
     
ani = animation.FuncAnimation(fig,update,range(0,len(xg),50), interval = 1000)

plt.show()
     