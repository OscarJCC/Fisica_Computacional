"""
Nombre: P01-OscarCastro Decaimiento Radioactivo
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

Este programa al ejecutarlo generara 5 graficas.
Primero se mostrara una gráfica, después para poder ver las 
siguientes grafica se debe cerrar la grafica que se esta 
mostrando para poder ir viendo las que siguen.

"""

import numpy as np
import plotly.graph_objects as pgo
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt

# Funciones------------------------------
     
def Metodo_De_Euler(Nu0,t0,tf,T,h,N):
     vg = [] # Lista para guardan las interaciones de Nu(t)
     tg = [] # Lista para guardar las interaciones del tiempo
     while t0 < tf:
          if t0 == 0:
               vg.append(Nu0)
               tg.append(t0)
          Nu0 = Nu0 - (Nu0/T)*h # Metodo de Euler
          vg.append(Nu0)
          t0 += h
          tg.append(t0)
     t0 = 0
     return Grafica(vg,tg,t0,tf,N)
     
def Grafica(v,t,t0,tf,N):     
     m = np.linspace(t0,tf,101)
     
     va = [] # Lista para guardar la evaluacion de la solucion analitica
     for i in m:
          x = i
          e = eval("100*np.exp(-x)") # evaluacion de la solucion analitica de la Ec. Dif.
          va.append(e)
          
     fig = pgo.Figure()
     fig.add_trace(pgo.Scatter(x = t, y = v, name = r"$Nu(t+h) = Nu(t) - \frac{Nu(t)}{T}h$", line_color = "yellow"))
     fig.add_trace(pgo.Scatter(x = m, y = va, name = r"$Nu(t) = 100e^{-t/T}$", mode = "markers", line_color = "purple"))
     fig.update_layout(title = N, template = "plotly_dark", xaxis_title  ="Tiempo (s)", yaxis_title ="Nu(t)")
     fig.show()
     
     #plt.style.use("dark_background") 
     #fig, g = plt.subplots(dpi = 110, figsize = (12.3,6.1), facecolor = "blue")
     #g.set_title(N, fontsize = 20)
     #g.set_xlabel("Tiempo (s)")
     #g.set_ylabel("Nu(t)")
     #g.grid(color = "blue")
     #g.axhline(color = "red")
     #g.axvline(color = "red")
     #g.plot(t,v, color = "yellow", label = r"$Nu(t+h) = Nu(t) - \frac{Nu(t)}{T}h$")
     #g.plot(m,va, "r--", color = "purple", label=r"$Nu(t) = 100e^{-t/T}$")
     #g.legend(edgecolor = "red", fontsize = 15)
     #plt.show()

#Variables------------------------------

Nu0 = 100 # Cantidad de nucleos inicial
T = 1     # Constante de decaimiento
t0 = 0    # Tiempo inicial
tf = 10   # Tiempo final

# Tamaños de paso
h1 = 1
h2 = 0.5
h3 = 0.1
h4 = 0.05
h5 = 0.01

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de la Ec. Dif.
# con los distintos tamaños de paso

Metodo_De_Euler(Nu0,t0,tf,T,h1,"Metodo de Euler <Grafica 1, Tamaño de paso h = 1>")
Metodo_De_Euler(Nu0,t0,tf,T,h2,"Metodo de Euler <Grafica 2, Tamaño de paso h = 0.5>")
Metodo_De_Euler(Nu0,t0,tf,T,h3,"Metodo de Euler <Grafica 3, Tamaño de paso h = 0.1>")
Metodo_De_Euler(Nu0,t0,tf,T,h4,"Metodo de Euler <Grafica 4, Tamaño de paso h = 0.05>")
Metodo_De_Euler(Nu0,t0,tf,T,h5,"Metodo de Euler <Grafica 5, Tamaño de paso h = 0.01>")
