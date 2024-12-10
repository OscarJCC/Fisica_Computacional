"""
Nombre: P11-OscarCastro El Péndulo Simple Euler-Cromer
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------

def Grados_A_Radianes(A0):
     return (A0*np.pi)/180

def Metodo_De_Euler(θ0,w0,t0,tf,h,N):
     global g, l, m, i
     
     θg = [θ0] # Lista para guardan las interaciones de θ(t) Euler
     tg = [t0] # Lista para guardar las interaciones del tiempo Euler
     θgc = [θ0] # Lista para guardan las interaciones de θ(t) Euler Cromer
     tgc = [t0] # Lista para guardar las interaciones del tiempo Euler Cromer
     w0c = w0
     θ0c = θ0
     t0c = t0
     while t0 < tf: # Metodo de Euler
          w0c = w0c - (g/l)*θ0c*h
          θ0c = θ0c + w0c*h
          
          θ0 = θ0 + w0*h
          w0 = w0 - (g/l)*θg[i-1]*h
          
          t0 += h
          t0c += h
          i += 1
          
          θg.append(θ0)
          tg.append(t0)
          θgc.append(θ0c)
          tgc.append(t0c)
     t0 = 0
     return Grafica(θg,tg,θgc,tgc,N)
     
def Grafica(θg,tg,θgc,tgc,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"\n"+r"$θ$ vs $t$", fontsize = 12)
     l1.set_xlabel(r"$t(s)$")
     l1.set_ylabel("$θ(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(tg,θg, color = "blue", label = "Euler")#r"$y(t+h) = y(t) + vh$")
     l1.plot(tgc,θgc, color = "yellow", label = "Euler Cromer")#r"$v(t+h) = v(t) - gh$")
     l1.legend(edgecolor = "red", fontsize = 15)
     
     plt.show()

#Variables------------------------------

θ0 = Grados_A_Radianes(11.5) # Angulo inicial
w0 = 0                       # Velocidad angular inicial
l = 1                        # Longitud del pendulo
g = 9.81                     # Aceleracion de la gravedad
t0 = 0                       # Tiempo inicial
tf = 10                      # Tiempo final
h = .001                     # Tamaños de paso
i = 0

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(θ0,w0,t0,tf,h,f"Metodo de Euler vs Metodo de Euler Cromer\nEl Péndulo Simple")