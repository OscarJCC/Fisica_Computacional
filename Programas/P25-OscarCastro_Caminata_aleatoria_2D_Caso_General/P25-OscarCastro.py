"""
Nombre: P25-OscarCastro Caminata Aleatoria 2D Caso General
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

def Caminata(n,nc,N):
     
     yg = [0]        # Matriz para guardar los pasos de las caminatas
     yg2 = [0]
     xg = np.arange(n+1)
     
     P = 0
     k = 0
     Px = 0
     Py = 0
     j = 1
     
     for i in range(n):
          while j <= nc:
               while k <= i:
                    r = rm.uniform(-1,1)
                    if r < -0.5: #-1 <= r < -0.5:
                         Px += 1
                    elif r >= -0.5 and r < 0: #-0.5 <= r < 0:
                         Py += 1
                    elif r >= 0 and r < 0.5: #0 <= r < 0.5:
                         Px -= 1
                    elif r >= 0.5: #0.5 <= r <= 1:
                         Py -= 1
                    k += 1
                    
               P += abs(np.sqrt(Px**2 + Py**2))
               k = 0
               Px = 0
               Py = 0
               j += 1
               
          yg.append(P/nc)
          yg2.append((P/nc)**2)
          P = 0
          k = 0
          Px = 0
          Py = 0
          j = 1
          
     ec1 = Regrecion(xg,yg,2)
     
     ec2 = Regrecion(xg,yg2,1)
     
     return Grafica(xg,yg,yg2,ec1,ec2,N,nc)
     
def Grafica(xg,yg,yg2,ec1,ec2,N,nc):
     xg = np.array(xg)
     
     col = ["white","blue"]
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$t$ vs $Promedio$", fontsize = 10)
     l1.set_xlabel(r"$t$")
     l1.set_ylabel("$Promedio$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "turquoise")
     l1.axvline(color = "turquoise")
     l1.plot(xg,yg,"--", color = "white", label = "Regresion no lineal")
     l1.plot(xg,ec1(xg), color = "blue", label = f"Ecuacion:\n"+"{}".format(ec1)+f"\n\nR = {pearsonr(yg,ec1(xg))[0]}")
     l1.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l2.set_title(N+"\n"+r"$t$ vs $Promedio^2$", fontsize = 15)
     l2.set_xlabel(r"$t$")
     l2.set_ylabel("$Promedio^2$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "turquoise")
     l2.axvline(color = "turquoise")
     l2.plot(xg,yg2,"--", color = "white", label = "Regresion lineal")
     l2.plot(xg,ec2(xg), color = "blue", label = f"Ecuacion:\n {str(ec2)}"+f"\n\nR = {pearsonr(yg,ec2(xg))[0]}")
     l2.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     plt.show()

# Variables------------------------------

n = 100# Numero de pasos
nc = 100 # Numerom de caminatas

N = "Caminata Aleatoria 2D Caso General"

Caminata(n,nc,N)