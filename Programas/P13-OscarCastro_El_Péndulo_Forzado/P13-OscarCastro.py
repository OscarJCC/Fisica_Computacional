"""
Nombre: P13-OscarCastro El Péndulo Forzado
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

def Metodo_De_Euler(θ0,w0,t0,tf,q,freqd,freqddr,fd,h,N):
     global g, l
     wg = [] # Matriz para guardar las interaciones de v(t)
     θg = [] # Matriz para guardan las interaciones de θ(t)
     tg = [] # Matriz para guardar las interaciones del tiempo
     fdr = [θ0]
     tr = [t0]
     t0r = t0
     tfr = tf
     w0r = w0
     θ0r = θ0
     while t0r < tfr:
               w0r = w0r - ((g/l)*θ0r + q*w0r - fd*np.sin(freqddr*t0r))*h # Metodo de Euler Cromer
               θ0r = θ0r + w0r*h
               t0r += h
               
               fdr.append(θ0r)
               tr.append(t0r)
          
     for i in range(len(freqd)):
          w = [w0] # Lista para guardar las interaciones de v(t)
          θ = [θ0] # Lista para guardan las interaciones de θ(t)
          t = [t0] # Lista para guardar las interaciones del tiempo
          while t0 < tf:
               w0 = w0 - ((g/l)*θ0 + q*w0 - fd*np.sin(freqd[i]*t0))*h # Metodo de Euler Cromer
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
          
     return Grafica(θg,fdr,tg,tr,N)
     
def Grafica(θg,fdr,tg,tr,N):
     color = ["purple","blue","yellow","turquoise"]
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"\n"+r"$θ$ vs $t$", fontsize = 12)
     l1.set_xlabel(r"$t(s)$")
     l1.set_ylabel("$θ(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     for j in range(len(freqd)):
          l1.plot(tg[j],θg[j], color = color[j], label = f"Para f{j+1} = {freqd[j]}")#r"$y(t+h) = y(t) + vh$")
     l1.legend(edgecolor = "red", fontsize = 15,  labelcolor = color)
     
     fig, l2 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l2.set_title(N+"\n"+r"$θ$ vs $t$", fontsize = 12)
     l2.set_xlabel(r"$t(s)$")
     l2.set_ylabel("$θ(t)$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(tr,fdr, color = "red", label = f"Frecuencia de resonancia = {freqddr}")#r"$y(t+h) = y(t) + vh$")
     l2.legend(edgecolor = "yellow", fontsize = 15,  labelcolor = "red")
     plt.show()

#Variables------------------------------

θ0 = Grados_A_Radianes(11.5)  # Angulo inicial
w0 = 0                        # Velocidad angular inicial
l = 1                         # Longitud del pendulo
m = 1                         # Masa
g = 9.81                      # Aceleracion de la gravedad
t0 = 0                        # Tiempo inicial
tf = 15                       # Tiempo final
h = .001                      # Tamaños de paso
q = 1                         # Parametro de amortiguamiento
freqd = [0.5,1,2,4]           # Frecuencia angular de la fuerza
freqddr = np.sqrt(g/l)        # Frecuencia de Resonancia
fd = 0.2                      # Fuerza de impulso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(θ0,w0,t0,tf,q,freqd,freqddr,fd,h,f"Metodo de Euler Cromer\nEl Péndulo Forzado")