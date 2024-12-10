"""
Nombre: P03-OscarCastro Movimiento En Caida Libre
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
     global g
     
     vg = [v0] # Liata para guardar las interaciones de v(t)
     yg = [y0] # Lista para guardan las interaciones de y(t)
     tg = [t0] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          v0 = v0 - g*h # Metodo de Euler
          y0 = y0 + v0*h 
          vg.append(v0)
          yg.append(y0)
          t0 += h
          tg.append(t0)
     t0 = 0
     return Grafica(yg,vg,tg,t0,tf,N)
     
def Grafica(yg,vg,tg,t0,tf,N):     
     m = np.linspace(t0,tf,1001)
     
     va = [] # Lista para guardar la evaluacion de la solucion analitica de la velocidad
     ya = [] # Lista para guardar la evaluacion de la solucion analitica de la posicion
     for t in m:
          ev = eval("v0 - g*t") # Evaluacion de la solucion analitica de la Ec. Dif. de la velocidad
          ey = eval("y0 + (v0 - (g*t)/2)*t") # Evaluacion de la solucion analitica de la Ec. Dif. de la posicion
          ya.append(ey)
          va.append(ev)
     
     plt.style.use("dark_background") 
     fig, (l1,l2) = plt.subplots(1,2,dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+" - Posicion", fontsize = 20)
     l1.set_xlabel("Tiempo (s)")
     l1.set_ylabel("y(t)")
     l1.grid(color = "blue")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(tg,yg, color = "yellow", label = "Solucion Numerica")#r"$y(t+h) = y(t) + vh$")
     l1.plot(m,ya, "r--", color = "purple", label = "Solucion Analitica")#r"$y(t) = y + vt - \frac{gt^2}{2}$")
     l1.legend(edgecolor = "red", fontsize = 15)
     
     #Grafica de la velocidad
     l2.set_title(N+" - Velocidad", fontsize = 20)
     l2.set_xlabel("Tiempo (s)")
     l2.set_ylabel("v(t)")
     l2.grid(color = "blue")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(tg,vg, color = "orange", label = "Solucion Numerica")#r"$v(t+h) = v(t) - gh$")
     l2.plot(m,va, "r--", color = "green", label = "Solucion Analitica")#r"$v(t) = v - gt$")
     l2.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

y0 = 15                   # Posicion inicial
v0 = 0                    # Velocidad inicial
g = 9.81                  # Aceleracion de la gravedad
t0 = 0                    # Tiempo inicial
tf = np.sqrt((2*y0)/g)    # Tiempo final
h = .01                   # Tamaños de paso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(y0,v0,t0,tf,h,f"Metodo de Euler\nCaida libre")