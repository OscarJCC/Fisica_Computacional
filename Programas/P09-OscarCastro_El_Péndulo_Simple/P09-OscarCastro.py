"""
Nombre: P09-OscarCastro El Péndulo Simple
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

def Metodo_De_Euler(E0,θ0,w0,t0,tf,h,N):
     global g, l, m
     
     wg = [w0] # Liata para guardar las interaciones de v(t)
     θg = [θ0] # Lista para guardan las interaciones de θ(t)
     Eg = [E0] # Lista para guardan las interaciones de E(t)
     tg = [t0] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          E0 = E0 + ((m*g*l)/(2))*(w0**2+(g/l)*θ0**2)*(h**2)
          w0 = w0 - (g/l)*θ0*h # Metodo de Euler
          θ0 = θ0 + w0*h
          
          t0 += h
          wg.append(w0)
          θg.append(θ0)
          Eg.append(E0)
          tg.append(t0)
     t0 = 0
     return Grafica(Eg,θg,wg,tg,t0,tf,N)
     
def Grafica(Eg,θg,wg,tg,t0,tf,N):     
     plt.style.use("dark_background") 
     fig, (l1,l2) = plt.subplots(2,1,dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"\n"+r"$θ$ vs $t$ y $E_t$ vs $t$", fontsize = 12)
     l1.set_xlabel(r"$t(s)$")
     l1.set_ylabel("$θ(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(tg,θg, color = "yellow")#, label = "Solucion Numerica")#r"$y(t+h) = y(t) + vh$")
     #l1.plot(m,ya, "r--", color = "purple", label = "Solucion Analitica")#r"$y(t) = y + vt - \frac{gt^2}{2}$")
     #l1.legend(edgecolor = "red", fontsize = 15)
     
     #Grafica de la velocidad
     #l2.set_title(N+"\nw vs t", fontsize = 15)
     l2.set_xlabel("$t(s)$")
     l2.set_ylabel(r"$E_t(t)$")
     l2.grid(color = "turquoise")
     l2.axhline(color = "red")
     l2.axvline(color = "red")
     l2.plot(tg,Eg, color = "yellow")#, label = "Solucion Numerica")#r"$v(t+h) = v(t) - gh$")
     ##l2.plot(m,va, "r--", color = "green", label = "Solucion Analitica")#r"$v(t) = v - gt$")
     #l2.legend(edgecolor = "red", fontsize = 15)
     plt.show()

#Variables------------------------------

θ0 = Grados_A_Radianes(11.5) # Angulo inicial
w0 = 0    # Velocidad angular inicial
l = 1     # Longitud del pendulo
m = 1     # Masa
g = 9.81  # Aceleracion de la gravedad
t0 = 0    # Tiempo inicial
tf = 10  # Tiempo final
h = .01   # Tamaños de paso
E0 = (m*w0**2*l**2)/2 + m*g*l*(θ0**2/2)   # Energia incial

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(E0,θ0,w0,t0,tf,h,f"Metodo de Euler\nEl Péndulo Simple")