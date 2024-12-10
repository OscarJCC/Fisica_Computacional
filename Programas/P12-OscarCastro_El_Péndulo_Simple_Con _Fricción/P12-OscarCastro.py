"""
Nombre: P12-OscarCastro El Péndulo Simple Con Friccion
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------

def Grados_A_Radianes(A):
     return (A*np.pi)/180

def Metodo_De_Euler(θ0,w0,t0,tf,q,h,N):
     global g, l
     wg = [] # Matriz para guardar las interaciones de v(t)
     θg = [] # Matriz para guardan las interaciones de θ(t)
     tg = [] # Matriz para guardar las interaciones del tiempo
     for i in range(len(q)):
          w = [w0] # Lista para guardar las interaciones de v(t)
          θ = [θ0] # Lista para guardan las interaciones de θ(t)
          t = [t0] # Lista para guardar las interaciones del tiempo
          while t0 < tf:
               w0 = w0 - ((g/l)*θ0+q[i]*w0)*h # Metodo de Euler Cromer
               θ0 = θ0 + w0*h
               t0 += h
               
               w.append(w0)
               θ.append(θ0)
               t.append(t0)
          
          wg.append(w)
          θg.append(θ)
          tg.append(t)
          
          w = []
          θ = []
          t = []
          
          t0 = 0
          w0 = 0
          θ0 = Grados_A_Radianes(11.5)
          
     return Grafica(θg,tg,N)
     
def Grafica(θg,tg,N):
     color = ["purple","blue","yellow"]
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"\n"+r"$θ$ vs $t$", fontsize = 12)
     l1.set_xlabel(r"$t(s)$")
     l1.set_ylabel("$θ(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     for j in range(len(q)):
          l1.plot(tg[j],θg[j], color = color[j], label = f"Para q{j+1} = {q[j]}")#r"$y(t+h) = y(t) + vh$")
     l1.legend(edgecolor = "red", fontsize = 15,  labelcolor = color)
     plt.show()

#Variables------------------------------

θ0 = Grados_A_Radianes(11.5)  # Angulo inicial
w0 = 0                        # Velocidad angular inicial
l = 1                         # Longitud del pendulo
m = 1                         # Masa
g = 9.81                      # Aceleracion de la gravedad
t0 = 0                        # Tiempo inicial
tf = 10                       # Tiempo final
h = .01                       # Tamaños de paso
q = [1,5,10]                  # Parametro de amortiguamiento

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(θ0,w0,t0,tf,q,h,f"Metodo de Euler Cromer\nEl Péndulo Simple Con Friccion")