"""
Nombre: P29-OscarCastro La Radiactividad 2 Enfoque Aleatorio
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats.stats import pearsonr
import random as rm
import winsound as ws
# Funciones------------------------------

def Regrecion(xg,yg,g):
     ecu = np.poly1d(np.polyfit(xg,yg,g))
     
     return ecu

def Radiactividad(n,p,h,tf,N):
     
     yg = []
     xg = np.arange(n)
     i = 0
     m = 0

     while i < tf:
          #print(f"Numero de nucleos = {n}")
          for j in range(n):
               r = rm.uniform(0,1)
               yg.append(r)
               
          for k in yg:
               if k <= p:
                    n -= 1
                    m += 1
                    ws.Beep(1000,50)
                    
          #print(f" Decaen {m}")
          m = 0
          yg = []
          i += 1
               
#     ec1 = Regrecion(xg,yg,2)
#     
#     ec2 = Regrecion(xg,yg2,1)
#     
#     return Grafica(xg,yg,N)
#     
#def Grafica(xg,yg,N):
#     
#     plt.style.use("dark_background") 
#     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
#     l1.set_title(N, fontsize = 10)
#     l1.set_xlabel(r"$t$")
#     l1.set_ylabel("$Promedio$")
#     l1.grid(color = "turquoise")
#     l1.axhline(color = "turquoise")
#     l1.axvline(color = "turquoise")
#     l1.plot(xg,yg,"--", color = "white")
#     l1.legend(edgecolor = "turquoise", fontsize = 10)
#     
#     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
#     l2.set_title(N+"\n"+r"$t$ vs $Promedio^2$", fontsize = 15)
#     l2.set_xlabel(r"$t$")
#     l2.set_ylabel("$Promedio^2$")
#     l2.grid(color = "turquoise")
#     l2.axhline(color = "turquoise")
#     l2.axvline(color = "turquoise")
#     l2.plot(xg,yg2,"--", color = "white", label = "Regresion lineal")
#     l2.plot(xg,ec2(xg), color = "blue", label = f"Ecuacion:\n {str(ec2)}"+f"\n\nR = {pearsonr(yg,ec2(xg))[0]}")
#     l2.legend(edgecolor = "turquoise", fontsize = 10, labelcolor = col)
#     plt.show()
#
# Variables------------------------------
n = 10000
p = 0.01
h = 1
tf = 60

N = "Radiactividad"

Radiactividad(n,p,h,tf,N)