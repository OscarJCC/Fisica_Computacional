"""
Nombre: P16-OscarCastro El Movimiento Planetario 2
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

def Metodo_De_Euler(x0,y0,vx0,vy0,t0,tf,h,N):
     global i,m,C
     xg = [] # Matriz para guardan las interaciones de posicion en x
     yg = [] # Matriz para guardan las interaciones de posicion en x
     tg = [] # Matriz para guardar las interaciones de tiempo
     C = []    # Lista par guardar el cociente t^2/a^2
     px = []   # Lista par guardar la posicion final del planeta en x
     py = []   # Lista par guardar la posicion final del planeta en y

     for j in range(len(x0)):
          print(j)
          xi = x0[j]
          yi = y0
          vxi = vx0
          vyi = vy0[j]
          x = [xi] # Lista para guardan las interaciones de
          y = [yi]
          t = [t0] # Lista para guardar las interaciones de
          r = np.sqrt(xi**2 + yi**2)
          
          while t0 < tf: # Metodo de Euler
               vyi = vyi - ((4*(np.pi**2)*yi)/(r**3))*h
               yi = yi + vyi*h

               vxi = vxi - ((4*(np.pi**2)*xi)/(r**3))*h
               xi = xi + vxi*h

               t0 += h
               r = np.sqrt(xi**2 + yi**2)

               x.append(xi)
               y.append(yi)
               t.append(t0)
               
               A = np.arccos(xi/r)
               
               if round(A,m[j]) == 0:
                    i += 1
                    if i == 2:
                         tf = t0
          
          px.append(xi)
          py.append(yi)
          
          xg.append(x)
          yg.append(y)
          tg.append(t)
          
          C.append(round((tf**2)/(max(yg[j])**3),2))
          
          t0 = 0
          tf = 30.1
          
          #i = 1
          if j == 2:
               i = 1
          else:
               i = 1
          
     return Grafica(xg,yg,tg,px,py,N)

def Grafica(xg,yg,tg,px,py,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     nom = ["Venus","Tierra","Marte","Jupiter","Saturno"]
     col = ["yellow","orange","green","red","brown","white"]
     # Grafica
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 12)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel("$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     for j in range(len(x0)):
          l1.plot(xg[j],yg[j],"--", color = col[j+1],ms = 1,lw = 1)
          l1.plot(px[j],py[j],"o", color = col[j+1], label = nom[j]+f"\nt = {round(max(tg[j]),2)} años\n"+r"$\frac{t^2}{a^3} = $"+f"{C[j]}",ms = 4, lw = .2)
     l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 10, labelcolor = col)
     
     plt.show()

#Variables------------------------------

x0 = np.array([.72,1,1.52,5.20,9.58])#,9.58,19.19,30.07,39.48])
v = np.array([35.02,29.78,24.08,13.07,9.67])#,9.67,6.81,5.48,4.74])

vx0 = 0
y0 = 0
vy0 = (2*np.pi)*(v/29.78)
t0 = 0                        # Tiempo inicial
tf = 31                       # Tiempo final
h = .001                      # Tamaños de paso
i = 1
m = [3,3,3,3,4]

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.

Metodo_De_Euler(x0,y0,vx0,vy0,t0,tf,h,f"Metodo de Euler Cromer\nEl Movimiento Planetario 2")