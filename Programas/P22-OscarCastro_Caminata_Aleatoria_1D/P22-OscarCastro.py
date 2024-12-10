"""
Nombre: P22-OscarCastro Caminata Aleatoria
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
import random as rm

# Funciones------------------------------

def Caminata(n,nc,N):
     
     yg = []        # Matriz para guardar los pasos de las caminatas
     xg = [np.arange(n)]*nc
     prom = 0      # Lista para guardar la distancia promedio de cada caminata
     j = 0
     P = 0

     for i in range(nc):
          y = [0]
          while j < n-1:
               r = rm.uniform(-0.5,0.5)
               if r > 0:
                    P += 1
               elif r <= 0:
                    P -= 1
               y.append(P)
               j += 1

          yg.append(y)
          prom += P
          j = 0
          P = 0
     
     return Grafica(xg,yg,prom,N)
     
def Grafica(xg,yg,prom,N):
     col = ["orange","green","red","brown","white"]
     plt.style.use("dark_background") 
     for i in range(nc):
          fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
          l1.set_title(N+"\n"+r"$n$ vs $x$", fontsize = 15)
          l1.set_xlabel(r"$n$")
          l1.set_ylabel("$x$")
          l1.grid(color = "turquoise")
          l1.axhline(color = "red")
          l1.axvline(color = "red")
          l1.plot(xg[i],yg[i],"--", color = col[i], label = f"Caminata {i+1}\nDistancia Promedio\nentre las caminatas = {prom/nc}\nPosicion final = {yg[i][-1]}")
          l1.plot(xg[i],yg[i],".", color = col[i])
          l1.legend(edgecolor = "red", fontsize = 10)
     plt.show()

# Variables------------------------------

n = 20 # Numero de pasos
nc = 5 # Numerom de caminatas

N = "Caminata Aleatoria 1D"

Caminata(n,nc,N)