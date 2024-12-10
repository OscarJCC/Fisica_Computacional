"""
Nombre: P04-OscarCastro Movimiento Con Velocidad No Lineal
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------
     
def Metodo_De_Euler(v0,t0,tf,h,N):
     global i 
     tf = 1000000
     vg = [v0] # Lista para guardan las interaciones de v(t)
     tg = [t0] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          v0 = v0 + (a - b*v0)*h # Metodo de Euler
          vg.append(v0)
          t0 += h
          tg.append(t0)
          if v0 >= vg[i] - h**2 and v0 <= vg[i] + h**2: # Criterio de paro cuando v(t) es aproximadamente contante
               tf = t0
          i += 1
     t0 = 0
     return Grafica(vg,tg,t0,tf,N)
     
def Grafica(vg,tg,t0,tf,N):     
     m = np.linspace(t0,tf,1001)
          
     plt.style.use("dark_background") 
     fig, g = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     g.set_title(N, fontsize = 20)
     g.set_xlabel("Tiempo (s)")
     g.set_ylabel("v(t)")
     g.grid(color = "blue")
     g.axhline(color = "red")
     g.axvline(color = "red")
     g.plot(tg,vg, color = "yellow", label = f"Velocidad Aproximadamente\nContante En\ntf = {round(tf,4)}\nvf = {round(vg[i],2)}")
     g.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

v0 = 0    # Velocidad inicial
a = 10    # Constante
b = 1     # Constante
t0 = 0    # Tiempo inicial
tf = 0
i = 0
h = .01   # Tamaños de paso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(v0,t0,tf,h,f"Metodo de Euler \nVelocidad")