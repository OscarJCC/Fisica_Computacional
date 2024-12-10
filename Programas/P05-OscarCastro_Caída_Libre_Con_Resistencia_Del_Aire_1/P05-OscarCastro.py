"""
Nombre: P05-OscarCastro Caída Libre Con Resistencia Del Aire 1
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------
     
def Metodo_De_Euler(y0,v0,t0,tf,h,N):
     global i, m, c, g
     tf = 10000000000
     yg = [y0] # Lista para guardan las interaciones de y(t)
     vg = [v0] # Lista para guardan las interaciones de v(t)
     tg = [t0] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          v0 = v0 + (g - (c*v0)/m)*h # Metodo de Euler
          y0 = y0 - v0*h
          vg.append(v0)
          yg.append(y0)
          t0 += h
          tg.append(t0)
          if v0 >= vg[i] - h**2 and v0 <= vg[i] + h**2: # Criterio de paro cuando v(t) es aproximadamente contante
               tf = t0
          i += 1
     t0 = 0
     return Grafica(yg,vg,tg,t0,tf,N)
     
def Grafica(yg,vg,tg,t0,tf,N):     
     m = np.linspace(t0,tf,1001)
     
     plt.style.use("dark_background") 
     fig, (l1,l2) = plt.subplots(1,2,dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"Posicion", fontsize = 15)
     l1.set_xlabel("Tiempo (s)")
     l1.set_ylabel("y(t)")
     l1.grid(color = "blue")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(tg,yg, color = "yellow", label = f"Altura\nyf = {round(yg[i],2)}")
     l1.legend(edgecolor = "red", fontsize = 15)
     
     #Grafica de la velocidad
     l2.set_title(N+"Velocidad", fontsize = 15)
     l2.set_xlabel("Tiempo (s)")
     l2.set_ylabel("v(t)")
     l2.grid(color = "blue")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(tg,vg, color = "yellow", label =  f"Velocidad Termimnal En\ntf = {round(tf,4)}\nvf = {round(vg[i],2)}")
     l2.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

y0 = 0    # Posicion inicial
v0 = 0    # Velocidad inicial
m = 68.1  # Masa del movil
c = 12.5  # Coeficiente de arrastre
g = 9.81  # Aceleracion de la gravedad
t0 = 0    # Tiempo inicial
tf = 0
i = 0
h = .001  # Tamaños de paso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(y0,v0,t0,tf,h,f"Metodo de Euler \nCaida Libre Con Resistencia\n")