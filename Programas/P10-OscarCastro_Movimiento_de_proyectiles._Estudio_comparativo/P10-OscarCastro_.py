"""
Nombre: P10 OscarCastro Movimiento De Proyectiles
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

def Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h,N):
     global j, g, Bm, a, Tem, alp
     
     # Matrices Sin Friccion
     xgs = []  # Matriz para guardar las interaciones de la lista x Sin Friccion
     ygs = []  # Matriz para guardar las interaciones de la lista y Sin Friccion
     tgs = []  # Matriz para guardar las interaciones de la lista t Sin Friccion
     vgs = []  # Matriz para guardar las interaciones de la lista v Sin Friccion
     
     # Matrices Con Friccion
     xgf = []  # Matriz para guardar las interaciones de la lista x Con Friccion
     ygf = []  # Matriz para guardar las interaciones de la lista y Con Friccion
     tgf = []  # Matriz para guardar las interaciones de la lista t Con Friccion
     vgf = []  # Matriz para guardar las interaciones de la lista v Con Friccion
     
     # Matrices Con Friccion Variable
     xgfv = []  # Matriz para guardar las interaciones de la lista x Con Friccion Variable
     ygfv = []  # Matriz para guardar las interaciones de la lista y Con Friccion Variable
     tgfv = []  # Matriz para guardar las interaciones de la lista t Con Friccion Variable
     vgfv = []  # Matriz para guardar las interaciones de la lista v Con Friccion Variable
     
     for j in range(len(A0)):
          tf = 100000000
          vx0 = v0*np.cos(Grados_A_Radianes(A0[j])) # Velocidad inicial en direccion x 
          vy0 = v0*np.sin(Grados_A_Radianes(A0[j])) # Velocidad inicial en direccion y
          v = np.sqrt((vx0)**2 + (vy0)**2)          # Velocida total
          
          #Variables Sin Friccion
          x0s = x0     # Posicion en x Sin Friccion
          y0s = y0     # Posicion en y Sin Friccion
          vx0s = vx0   # Velocidad inicial en direccion x Sin Friccion
          vy0s = vy0   # Velocidad inicial en direccion y Sin Friccion
          vs = v       # Velocida total Sin Friccion
          t0s = t0     # Tiempo inicial Sin Friccion
          tfs = tf     # Tiempo final Sin Friccion
          
          xs = [x0s]   # Lista para guardar las interaciones de x(t) Sin Friccion
          ys = [y0s]   # Lista para guardar las interaciones de y(t) Sin Friccion
          ts = [t0s]   # Lista para guardar las interaciones del tiempo Sin Friccion
          vts = [vs]   # Lista para guardar las interaciones del v(t) Sin Friccion
          
          #Variables Con Friccion
          x0f = x0     # Posicion en x Con Friccion
          y0f = y0     # Posicion en y Con Friccion
          vx0f = vx0   # Velocidad inicial en direccion x Con Friccion
          vy0f = vy0   # Velocidad inicial en direccion y Con Friccion
          vf = v       # Velocida total Con Friccion
          t0f = t0     # Tiempo inicial Con Friccion
          tff = tf     # Tiempo final Con Friccion
          
          xf = [x0f]   # Lista para guardar las interaciones de x(t) Con Friccion
          yf = [y0f]   # Lista para guardar las interaciones de y(t) Con Friccion
          tcf = [t0f]  # Lista para guardar las interaciones del tiempo Con Friccion
          vtf = [vf]   # Lista para guardar las interaciones del v(t) Con Friccion
          
          #Variables Con Friccion Variable
          x0fv = x0     # Posicion en x Con Friccion Variable
          y0fv = y0     # Posicion en y Con Friccion Variable
          vx0fv = vx0   # Velocidad inicial en direccion x Con Friccion Variable
          vy0fv = vy0   # Velocidad inicial en direccion y Con Friccion Variable
          vfv = v       # Velocida total Con Friccion Variable
          t0fv = t0     # Tiempo inicial Con Friccion Variable
          tffv = tf     # Tiempo final Con Friccion Variable
          
          xfv = [x0f]   # Lista para guardar las interaciones de x(t) Con Friccion Variable
          yfv = [y0f]   # Lista para guardar las interaciones de y(t) Con Friccion Variable
          tfv = [t0f]  # Lista para guardar las interaciones del tiempo Con Friccion Variable
          vtfv = [vfv]   # Lista para guardar las interaciones del v(t) Con Friccion Variable
          
          
          while t0s < tfs:# Metodo Euler Sin Friccion
               vx0s = vx0s
               x0s = x0s + vx0s*h
               vy0s = vy0s - g*h
               y0s = y0s + vy0s*h
               t0s += h
               vs = np.sqrt((vx0s)**2 + (vy0s)**2)
               xs.append(x0s)
               ys.append(y0s)
               ts.append(t0s)
               vts.append(vs)
               if y0s < 0: # Criterio de paro
                    tfs = t0s
                    
          while t0f < tff: # Metodo de Euler Con Friccion
               vx0f = vx0f - Bm*vf*vx0f*h
               x0f = x0f + vx0f*h
               vy0f = vy0f - (g + Bm*vf*vy0f)*h
               y0f = y0f + vy0f*h
               t0f += h
               vf = np.sqrt((vx0f)**2 + (vy0f)**2)
               xf.append(x0f)
               yf.append(y0f)
               tcf.append(t0f)
               vtf.append(vf)
               if y0f < 0: # Criterio de paro
                    tff = t0f
          
          while t0fv < tffv: # Metodo de Euler Con Friccion Variable
               vx0fv = vx0fv - Bm*vfv*vx0fv*((1-((a*y0fv)/(Tem)))**alp)*h
               x0fv = x0fv + vx0fv*h
               vy0fv = vy0fv - g*h - Bm*vfv*vy0fv*((1-((a*y0fv)/(Tem)))**alp)*h
               y0fv = y0fv + vy0fv*h
               t0fv += h
               vfv = np.sqrt((vx0fv)**2 + (vy0fv)**2)
               xfv.append(x0fv)
               yfv.append(y0fv)
               tfv.append(t0fv)
               vtfv.append(vfv)
               if y0fv < 0: # Criterio de paro
                    tffv = t0fv
                    
          # Guardado en matrices Sin Friccion
          xgs.append(xs)
          ygs.append(ys)
          tgs.append(ts)
          vgs.append(vts)
          
          # Guardado en matrices Con Friccion
          xgf.append(xf)
          ygf.append(yf)
          tgf.append(tcf)
          vgf.append(vtf)
          
          # Guardado en matrices Con Friccion Variable
          xgfv.append(xfv)
          ygfv.append(yfv)
          tgfv.append(tfv)
          vgfv.append(vtfv)
          
          # Reinicio de Variables Sin Friccion          
          xs = [] 
          ys = [] 
          ts = []
          vts = []
          
          # Reinicio de Variables Con Friccion          
          xf = [] 
          yf = [] 
          tcf = []
          vtf = []
          
          # Reinicio de Variables Con Friccion Variable      
          xfv = [] 
          yfv = [] 
          tfv = []
          vtfv = []
         
     return Grafica(xgs,ygs,vgs,tgs,xgf,ygf,vgf,tgf,xgfv,ygfv,vgfv,tgfv,N)
     
def Grafica(xgs,ygs,vgs,tgs,xgf,ygf,vgf,tgf,xgfv,ygfv,vgfv,tgfv,N):
     j = 0
     color = ["white","gray","brown","purple","blue","green","yellow","orange","pink"]
     
     plt.style.use("fast")
     for j in range(len(A0)):
          #Grafica de la v_y vs t
          fig, l1 = plt.subplots(dpi = 110, figsize = (12.3,6.1))#, facecolor = "blue")
          l1.set_title(N+fr"$v$ vs $t$ - Angulo = ${A0[j]}°$", fontsize = 15)
          l1.set_xlabel(r"$t(s)$")
          l1.set_ylabel("$v(t)$")
          l1.grid(color = "black")
          l1.axhline(color = "red")
          l1.axvline(color = "red")
          l1.plot(tgs[j],vgs[j], color = "purple", label = "Sin Friccion")
          l1.plot(tgf[j],vgf[j], color = "blue", label = "Con Friccion")
          l1.plot(tgfv[j],vgfv[j], color = "green", label = "Con Friccion Variable")
          l1.legend(edgecolor = "red", fontsize = 15)
          
          # Grafica de la y vs x
          fig, l0 = plt.subplots(dpi = 110, figsize = (12.3,6.1))#, facecolor = "blue")
          l0.set_title(N+fr"$y$ vs $x$ - Angulo = ${A0[j]}°$", fontsize = 15)
          l0.set_xlabel(r"$x(t)$")
          l0.set_ylabel(r"$y(t)$")
          l0.grid(color = "black")
          l0.axhline(color = "red")
          l0.axvline(color = "red")
          l0.plot(xgs[j],ygs[j], color = "purple", label = "Sin Friccion")
          l0.plot(xgf[j],ygf[j], color = "blue", label = "Con Friccion")
          l0.plot(xgfv[j],ygfv[j], color = "green", label = "Con Friccion Variable")
          l0.legend(edgecolor = "red", fontsize = 15)
     
     plt.show()

#Variables------------------------------

x0 = 0    # Posicion inicial
y0 = 0    # Altura inicial
v0 = 700  # Velocidad inicial
t0 = 0    # Tiempo inicial
tf = 0
Bm = 4e-5
g = 9.81  # Aceleracion de la gravedad
a = 6.5e-3
Tem = 293.15 # Temperatura al nivel del mar (K)
alp = 2.5
h = .01   # Tamaño de paso

#Iteradores
i = 0
j = 0

# Angulos de proyeccion inicial
A0 = [10,20,30,40,50,60,70,80,85]

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h,f"Metodo de Euler\nMovimiento De Proyectiles\n")