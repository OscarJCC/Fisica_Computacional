"""
Nombre: P26-OscarCastro Caminata Aleatoria Autoevitante
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
     Py = 0
     P = 0
     for i in range(nc):
          y = [0]
          x = [0]
          while j <= n:
               r = rm.uniform(-1,1)
               if r < -0.5: #-1 <= r < -0.5:
                    Px += 1
               elif r >= -0.5 and r < 0: #-0.5 <= r < 0:
                    Py += 1
               elif r >= 0 and r < 0.5: #0 <= r < 0.5:
                    Px -= 1
               elif r >= 0.5: #0.5 <= r <= 1:
                    Py -= 1
               y.append(Py)
               x.append(Px)
               for k in range(len(y)-1):
                    if Px == x[k] and Py == y[k]:
                         y = [0]
                         x = [0]
                         j = 0
                         Py = 0
                         Px = 0
                         P = 0
                         break
               j += 1
          yg.append(y)
          xg.append(x)
          j = 0
          Py = 0
          Px = 0
          P = 0
     
     return Grafica(xg,yg,prom,N)
     
def Grafica(xg,yg,prom,N):
     #col = ["orange","green","purple","blue","red"]
     plt.style.use("dark_background") 
     for i in range(nc):
          fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
          l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 15)
          l1.set_xlabel(r"$x$")
          l1.set_ylabel("$y$")
          #l1.grid(color = "turquoise")
          l1.axhline(color = "turquoise")
          l1.axvline(color = "turquoise")
          l1.plot(xg[i],yg[i],"--", color = "blue")#, color = col[i], label = f"Caminata {i+1}\nDistancia Recorrida = {round(np.sqrt((yg[i][-1])**2 + (xg[i][-1])**2),3)}\nPosicion final = {(yg[i][-1],xg[i][-1])}")
          l1.plot(xg[i],yg[i],".", color = "blue")#, color = col[i])
          #l1.legend(edgecolor = "turquoise", fontsize = 10)#, labelcolor = col[i])
     plt.show()

# Variables------------------------------

n = 30 # Numero de pasos
nc = 5 # Numero de caminatas

N = "Caminata Aleatoria Autoevitante"

Caminata(n,nc,N)