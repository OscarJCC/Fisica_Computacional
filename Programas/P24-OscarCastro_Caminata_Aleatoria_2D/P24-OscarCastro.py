"""
Nombre: P22-OscarCastro Caminata Aleatoria 2D
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
     xg = []
     prom = 0      # Lista para guardar la distancia promedio de cada caminata
     j = 0
     Px = 0
     Py = n
     P = 0
     for i in range(nc):
          y = [0]
          x = [0]
          while j < n-1:
               r = rm.uniform(0,1)
               if r < 0.15: #-1 <= r < -0.5:
                    Px += 1
                    P += 1
               elif r >= 0.15 and r < 0.25: #-0.5 <= r < 0:
                    Py += 1
                    P += 1
               elif r >= 0.25 and r < 0.4: #0 <= r < 0.5:
                    Px -= 1
                    P -= 1
               elif r >= 0.4: #0.5 <= r <= 1:
                    Py -= 1
                    P -= 1
               y.append(Py)
               x.append(Px)
               j += 1
          prom = P   
          yg.append(y)
          xg.append(x)
          j = 0
          Py = 0
          Px = 0
     
     return Grafica(xg,yg,prom,N)
     
def Grafica(xg,yg,prom,N):
     col = ["orange","green","purple","blue","red"]
     plt.style.use("dark_background") 
     for i in range(nc):
          fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
          l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 15)
          l1.set_xlabel(r"$x$")
          l1.set_ylabel("$y$")
          #l1.grid(color = "turquoise")
          l1.axhline(color = "turquoise")
          l1.axvline(color = "turquoise")
          l1.plot(xg[i],yg[i],"--", color = col[i], label = f"Caminata {i+1}\nDistancia Recorrida = {round(np.sqrt((yg[i][-1])**2 + (xg[i][-1])**2),3)}\nPosicion final = {(yg[i][-1],xg[i][-1])}")
          l1.plot(xg[i],yg[i],".", color = col[i])
          l1.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col[i])
     plt.show()

# Variables------------------------------

n = 20 # Numero de pasos
nc = 5 # Numerom de caminatas

N = "Caminata Aleatoria 2D"

Caminata(n,nc,N)