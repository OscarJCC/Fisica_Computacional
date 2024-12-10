"""
Nombre: P23-OscarCastro Caminata Aleatoria 1D Caso General
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
     
     yg = [0]        # Lista para guardar los distancia promedio de las caminatas
     yg2 = [0]
     xg = np.arange(n+1)
     
     prom = 0
     k = 0
     P = 0
     j = 1
     for i in range(n):
          #print(f"Pasos = {i+1}-----------------------------------------------------------------")
          while j <= nc:
               #print(f"Caminata = {j}")
               while k <= i:
                    r = rm.uniform(-0.5,0.5)
                    if r > 0:
                         P += 1
                    elif r <= 0:
                         P -= 1
                    k += 1
               #print(F"Distancia de camipnata {j} con {k} pasos = {P}")
               prom += abs(P)
               k = 0
               P = 0
               j += 1
          #print(prom/nc)
          yg.append(prom/nc)
          yg2.append((prom/nc)**2)
          prom = 0
          k = 0
          P = 0
          j = 1
     
          
     return Grafica(xg,yg,yg2,N,nc)
     
def Grafica(xg,yg,yg2,N,nc):
     col = ["orange","green","red","brown","white"]
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l1.set_title(N+"\n"+r"$n$ vs $Promedio$", fontsize = 15)
     l1.set_xlabel(r"$n$")
     l1.set_ylabel(r"$Promedio$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xg,yg,"--", color = "white")
     l1.legend(edgecolor = "red", fontsize = 10)
     
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     l2.set_title(N+"\n"+r"$n$ vs $Promedio$", fontsize = 15)
     l2.set_xlabel(r"$n$")
     l2.set_ylabel(r"$Promedio$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(xg,yg2,"--", color = "white")
     l2.legend(edgecolor = "red", fontsize = 10)
     plt.show()

# Variables------------------------------

n = 100 # Numero de pasos
nc = 100 # Numero de caminatas

N = "Caminata Aleatoria 1D"

Caminata(n,nc,N)