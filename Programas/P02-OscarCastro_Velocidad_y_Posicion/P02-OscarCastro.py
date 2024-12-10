"""
Nombre: P02-OscarCastro Velocidad y Posicion
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------
     
def Metodo_De_Euler(x0,v0,t0,tf,h,N):
     xg = [] # Lista para guardan las interaciones de x(t)
     tg = [] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          if t0 == 0:
               xg.append(x0)
               tg.append(t0)
          x0 = x0 + v0*h # Metodo de Euler
          xg.append(x0)
          t0 += h
          tg.append(t0)
     t0 = 0
     return Grafica(xg,tg,t0,tf,N)
     
def Grafica(xg,tg,t0,tf,N):     
     m = np.linspace(t0,tf,1001)
     
     xa = [] # Lista para guardar la evaluacion de la solucion analitica
     for i in m:
          l = i
          e = eval("v0*l") # evaluacion de la solucion analitica de la Ec. Dif.
          xa.append(e)
          
     plt.style.use("dark_background") 
     fig, g = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     g.set_title(N, fontsize = 20)
     g.set_xlabel("Tiempo (s)")
     g.set_ylabel("x(t)")
     g.grid(color = "blue")
     g.axhline(color = "red")
     g.axvline(color = "red")
     g.plot(tg,xg, color = "yellow", label = r"$x(t+h) = x(t) + vh$")
     g.plot(m,xa, "r--", color = "purple", label=r"$x(t) = vt$")
     g.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

x0 = 0    # Posicion inicial
v0 = 40   # Velocidad inicial
t0 = 0    # Tiempo inicial
tf = 5    # Tiempo final
h = 1   # Tamaños de paso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0,v0,t0,tf,h,f"Metodo de Euler \nPosicion")