"""
Nombre: P20-OscarCastro El Movimiento Planetario 6
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Runge Kutta 4----------------

"""

import numpy as np
import matplotlib.pyplot as plt

# Funciones------------------------------

def F(ecuacion,x,y,vx,vy,c):
     r = np.sqrt((x0)**2 + (y0)**2)
     return eval(str(ecuacion))

def Runge_Kutta_4(x0,y0,vx0,vy0,t0,tf,h,N):
     global i
     xg = [x0] # Lista para guardan las interaciones de posicion en x
     yg = [y0] # Lista para guardan las interaciones de posicion en x
     tg = [t0] # Lista para guardar las interaciones de tiempo
     xge = [x0] # Lista para guardan las interaciones de posicion en x
     yge = [y0] # Lista para guardan las interaciones de posicion en x
     tge = [t0] # Lista para guardar las interaciones de tiempo
     x0e = x0
     y0e = y0
     vx0e = vx0
     vy0e = vy0
     re = np.sqrt(x0e**2 + y0e**2)
     c = -4*np.pi**2
     fvx = "c*(x/r**3)"
     fx = "vx"
     fvy = "c*(y/r**3)"
     fy = "vy"
     while t0 < tf: # Metodo de Runge_Kutta_4 vs Metodo Euler Cromer
          vy0e = vy0e - ((4*(np.pi**2)*y0e)/(re**3))*h
          y0e = y0e + vy0e*h
          
          vx0e = vx0e - ((4*(np.pi**2)*x0e)/(re**3))*h
          x0e = x0e + vx0e*h
          
          re = np.sqrt(x0e**2 + y0e**2)
          
          l1x = h*F(fvx,x0,y0,vx0,vy0,c)
          k1x = h*F(fx,x0,y0,vx0,vy0,c)
          l1y = h*F(fvy,x0,y0,vx0,vy0,c)
          k1y = h*F(fy,x0,y0,vx0,vy0,c)
          
          l2x = h*F(fvx,x0 + (k1x/2),y0 + (k1y/2),vx0 + (l1x/2),vy0 + (l1y/2),c)
          k2x = h*F(fx,x0 + (k1x/2),y0 + (k1y/2),vx0 + (l1x/2),vy0 + (l1y/2),c)
          l2y = h*F(fvy,x0 + (k1x/2),y0 + (k1y/2),vx0 + (l1x/2),vy0 + (l1y/2),c)
          k2y = h*F(fy,x0 + (k1x/2),y0 + (k1y/2),vx0 + (l1x/2),vy0 + (l1y/2),c)

          l3x = h*F(fvx,x0 + (k2x/2),y0 + (k2y/2),vx0 + (l2x/2),vy0 + (l2y/2),c)
          k3x = h*F(fx,x0 + (k2x/2),y0 + (k2y/2),vx0 + (l2x/2),vy0 + (l2y/2),c)
          l3y = h*F(fvy,x0 + (k2x/2),y0 + (k2y/2),vx0 + (l2x/2),vy0 + (l2y/2),c)
          k3y = h*F(fy,x0 + (k2x/2),y0 + (k2y/2),vx0 + (l2x/2),vy0 + (l2y/2),c)
          
          l4x = h*F(fvx,x0 + k3x,y0 + k3y,vx0 + l3x,vy0 + l3y,c)
          k4x = h*F(fx,x0 + k3x,y0 + k3y,vx0 + l3x,vy0 + l3y,c)
          l4y = h*F(fvy,x0 + k3x,y0 + k3y,vx0 + l3x,vy0 + l3y,c)
          k4y = h*F(fy,x0 + k3x,y0 + k3y,vx0 + l3x,vy0 + l3y,c)
          
          vx0 = vx0 + 1/6*(l1x + 2*l2x + 2*l3x + l4x)
          x0 = x0 + 1/6*(k1x + 2*k2x + 2*k3x + k4x)
          vy0 = vy0 + 1/6*(l1y + 2*l2y + 2*l3y + l4y)
          y0 = y0 + 1/6*(k1y + 2*k2y + 2*k3y + k4y)

          t0 += h
          i += 1
          
          xg.append(x0)
          yg.append(y0)
          tg.append(t0)
          xge.append(x0e)
          yge.append(y0e)

     return Grafica(xg,yg,xge,yge,tg,N)

     
def Grafica(xg,yg,xge,yge,tg,N):     
     plt.style.use("dark_background") 
     fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     
     # Grafica de la posicion
     l1.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 12)
     l1.set_xlabel(r"$x(t)$")
     l1.set_ylabel(r"$y(t)$")
     l1.grid(color = "turquoise")
     l1.axhline(color = "red")
     l1.axvline(color = "red")
     l1.plot(xge,yge,"-", color = "yellow", label = "Metodo de\nEuler Cromer")
     l1.plot(xg,yg,"--", color = "blue", label = "Metodo de\nRunge Kutta 4")
     l1.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1.plot(xg[i],yg[i],"o", color = "green", label = "Tierra",ms = 5)
     l1.axis("equal") #Ajuatr ejes
     l1.legend(edgecolor = "red", fontsize = 15)
     
     plt.show()

#Variables------------------------------

x0 = 1                        # Posicion inicial en x
v = 29.78
vx0 = 0                       # Velocidad inicial en x
y0 = 0                        # Posicion inicial en y
vy0 = (2*np.pi)*(v/29.78)     # Velocidad inicial en y
t0 = 0                        # Tiempo inicial
tf = 1                        # Tiempo final
h = .001                      # Tamaños de paso
i = 0

# Aplicacion del Metodo de Runge Kutta 4 para encontrar la solucion numerica de la Ec. Dif.

Runge_Kutta_4(x0,y0,vx0,vy0,t0,tf,h,f"Metodo de Runge Kutta 4 vs Metodo de Euler Cromer\nEl Movimiento Planetario 6")