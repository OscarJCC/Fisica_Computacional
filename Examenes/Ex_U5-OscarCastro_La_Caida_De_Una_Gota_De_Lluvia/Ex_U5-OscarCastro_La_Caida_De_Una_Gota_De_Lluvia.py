"""
Nombre: Ex_U5-OscarCastro La Caida De Una Gota De Lluvia
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import random as rm

# Funciones------------------------------
def Regrecion(xg,yg,g):
     ecu = np.poly1d(np.polyfit(xg,yg,g))
     return ecu

def Relaciones(n,nc,N):
     yg = []        # Matriz para guardar los pasos de las caminatas
     yg2 = []
     xg = np.arange(n)
     
     P = 0
     pm = 0
     k = 0
     Px = 0
     Py = 0
     k = 1
     
     for i in range(n):
          Py = i
          while k <= nc:
               while Py > 0:
                    r = rm.uniform(0,1)
                    if r < 0.15:
                         Px += 1
                         P += 1
                    elif r >= 0.15 and r < .25:
                         Py += 1
                         P += 1
                    elif r >= 0.25 and r < 0.4:
                         Px -= 1
                         P += 1
                    elif r >= 0.4:
                         Py -= 1
                         P += 1
               pm += P
               Px = 0
               Py = i
               k += 1
               P = 0

          yg.append(pm/nc)
          yg2.append((pm/nc))
          P = 0
          pm = 0
          Px = 0
          k = 1
          
     ec1 = Regrecion(xg,yg,1)
     
     ec2 = Regrecion(xg,yg2,2)
     
     return GraficaR(xg,yg,yg2,ec1,ec2,N,nc)
     
def Caminatas(n,nc,N):
     
     yg = []
     xg = []
     tc = []
     j = 1
     Px = 0
     Py = n
     P = 0
     while j <= nc:
          y = [n]
          x = [0]
          while Py > 0:
               r = rm.uniform(0,1)
               if r < 0.15:
                    Px += 1
                    P += 1
               elif r >= 0.15 and r < 0.25:
                    Py += 1
                    P += 1
               elif r >= 0.25 and r < 0.4:
                    Px -= 1
                    P += 1
               elif r >= 0.4:
                    Py -= 1
                    P += 1
               y.append(Py)
               x.append(Px)
          tc.append(P)   
          yg.append(y)
          xg.append(x)
          P = 0
          Py = n
          Px = 0
          j += 1
     
     return GraficaC(xg,yg,tc,N)
     
def GraficaC(xg,yg,tc,N):
     col = ["orange","green","purple","blue","red"]
     plt.style.use("dark_background") 
     for i in range(5):
          fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
          l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 15)
          l1.set_xlabel(r"$x$")
          l1.set_ylabel("$y$")
          #l1.grid(color = "turquoise")
          l1.axhline(color = "turquoise")
          l1.axvline(color = "turquoise")
          l1.plot(xg[i],yg[i],"--", color = col[i], label = f"Gota {i+1}\nTiempo de Caida = {tc[i]}s")
          l1.plot(xg[i],yg[i],".", color = col[i])
          l1.axis("equal")
          l1.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col[i])
     plt.show()

def GraficaR(xg,yg,yg2,ec1,ec2,N,nc):
     xg = np.array(xg)
     
     col = ["white","blue"]
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$h$ vs $t$", fontsize = 10)
     l1.set_xlabel(r"$h$")
     l1.set_ylabel("$t$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "turquoise")
     l1.axvline(color = "turquoise")
     l1.plot(xg,ec1(xg), color = "blue", label = f"Ecuacion:\n"+"{}".format(ec1)+f"\n\nR = {pearsonr(yg,ec1(xg))[0]}")
     l1.plot(xg,yg,"--", color = "white", label = "Regresion lineal")
     l1.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     
     #fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     #l2.set_title(N+"\n"+r"$t$ vs $Promedio^2$", fontsize = 15)
     #l2.set_xlabel(r"$t$")
     #l2.set_ylabel("$Promedio^2$")
     #l2.grid(color = "turquoise")
     #l2.axhline(color = "turquoise")
     #l2.axvline(color = "turquoise")
     #l2.plot(xg,yg2,"--", color = "white", label = "Regresion no lineal")
     #l2.plot(xg,ec2(xg), color = "blue", label = f"Ecuacion:\n {str(ec2)}"+f"\n\nR = {pearsonr(yg,ec2(xg))[0]}")
     #l2.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     plt.show()
# Variables------------------------------

n = 100 # Numero de pasos
nc = 100 # Numero de caminatas

N = "La Caida De Una Gota De Lluvia"

Caminatas(n,nc,N)

Relaciones(n,nc,N)