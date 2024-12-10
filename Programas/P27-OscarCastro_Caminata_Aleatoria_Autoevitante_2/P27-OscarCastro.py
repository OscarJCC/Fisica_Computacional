"""
Nombre: P27-OscarCastro Caminata Aleatoria Autoevitante 2
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
     
     yg = [0]
     yg2 = [0]
     vF = [3/4]*4
     vFprom = (3/4)*4
     xg = np.arange(n+1)
     
     P = 0
     k = 0
     l = 0
     j = 1
     Px = 0
     Py = 0
     m = 0
     
     for i in range(n):
          while j <= nc:
               y = [0]
               x = [0]
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
                    y.append(Py)
                    x.append(Px)
                    for l in range(len(y)-1):
                         if Px == x[l] and Py == y[l]:
                              y = [0]
                              x = [0]
                              k = 0
                              Py = 0
                              Px = 0
                              m = 0
                              break
                    k += 1
               P += abs(np.sqrt(Px**2 + Py**2))
               k = 0
               j += 1
               Py = 0
               Px = 0
               m = 0
          yg.append(P/nc)
          yg2.append((P/nc)**2)
          if i > 2:
               vF.append(np.log10(yg2[-1])/(2*(np.log10(i))))
               vFprom += vF[-1]
          P = 0
          k = 0
          j = 1
          Py = 0
          Px = 0
          m = 0
     
     
     ec1 = Regrecion(xg,yg,2)
     
     ec2 = Regrecion(xg,yg2,2)
     
     ec3 = Regrecion(xg,vF,1)
     
     return Grafica(xg,yg,yg2,vF,vFprom,ec1,ec2,ec3,N,nc)
     
def Grafica(xg,yg,yg2,vF,vFprom,ec1,ec2,ec3,N,nc):
     xg = np.array(xg)
     
     col = ["white","blue"]
     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$n$ vs $Promedio$", fontsize = 15)
     l1.set_xlabel(r"$n$")
     l1.set_ylabel("$Promedio$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xg,yg,"--", color = "white", label = "Regresion no lineal")
     l1.plot(xg,ec1(xg), color = "blue", label = f"Ecuacion:\n"+"{}".format(ec1)+f"\n\nR = {round(pearsonr(yg,ec1(xg))[0],4)}")
     l1.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l2.set_title(N+"\n"+r"$n$ vs $Promedio^2$", fontsize = 15)
     l2.set_xlabel(r"$n$")
     l2.set_ylabel("$Promedio^2$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(xg,yg2,"--", color = "white", label = "Regresion lineal")
     l2.plot(xg,ec2(xg), color = "blue", label = f"Ecuacion:\n {str(ec2)}"+f"\n\nR = {round(pearsonr(yg,ec2(xg))[0],4)}")
     l2.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     
     fig, l3 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l3.set_title(N+"\n"+r"$n$ vs Exponente de Flory", fontsize = 15)
     l3.set_xlabel(r"$n$")
     l3.set_ylabel("$Exponente$ $de$ $Flory$")
     l3.grid(color = "turquoise")
     l3.axhline(color = "red")
     l3.axvline(color = "red")
     l3.plot(xg,vF,"--", color = "white", label = f"Exponente de Flory "+r"$(v)$"+"\n"+"$v$"+f" promedio es {round(vFprom/n,3)}")
     #l3.plot(xg,ec3(xg), color = "blue", label = f"Ecuacion:\n {str(ec3)}"+f"\n\nR = {pearsonr(yg,ec3(xg))[0]}")
     l3.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
     plt.show()

# Variables------------------------------

n = 20 # Numero de pasos
nc = 100  # Numero de caminatas

N = "Caminata Aleatoria Autoevitante 2"

Caminata(n,nc,N)