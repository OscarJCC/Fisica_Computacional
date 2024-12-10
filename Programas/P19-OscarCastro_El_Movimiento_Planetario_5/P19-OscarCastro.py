"""
Nombre: P19-OscarCastro_El_Movimiento_Planetario_5
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

-------------Metodo de Euler----------------

"""

# Librerias
from tkinter import *
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Funciones de Calculos Matematicos

def Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h):
     global i, xgt, ygt, xgj, ygj, tg

     xgt = [] # Matriz para guardan las interaciones de posicion en x tierra
     ygt = [] # Matriz para guardan las interaciones de posicion en y tierra
     
     xgj = [] # Matriz para guardan las interaciones de posicion en x jupiter
     ygj = [] # Matriz para guardan las interaciones de posicion en y jupiter
     
     tg = [] # Matriz para guardar las interaciones de tiempo

     rt = np.sqrt(x0t**2 + y0t**2)                          # Radio sol tierra
     rj = np.sqrt(x0j**2 + y0j**2)                          # Radio sol jupiter
     rtj = np.sqrt(abs((x0t - x0j)**2 - (y0t - y0j)**2))    # Radio tierra jupiter
     
     Cjs = mj/ms
     Cts = mt/ms
     
     while t0 < tf: # Metodo de Euler

          vx0t = vx0t - 4*(np.pi**2)*(x0t/(rt**3) + (Cjs)*((x0t-x0j)/(rtj**3)))*h # Iteracion de velocidad en x de la tierra
          vx0j = vx0j - 4*(np.pi**2)*(x0j/(rj**3) + (Cts)*((x0j-x0t)/(rtj**3)))*h # Iteracion de velocidad en x de jupiter
          
          x0t = x0t + vx0t*h # Iteracion de la posicion en x de la tierra
          x0j = x0j + vx0j*h # Iteracion de la posicion en x jupiter

          vy0t = vy0t - 4*(np.pi**2)*(y0t/(rt**3) + (Cjs)*((y0t-y0j)/(rtj**3)))*h # Iteracion de velocidad en x de la tierra
          vy0j = vy0j - 4*(np.pi**2)*(y0j/(rj**3) + (Cts)*((y0j-y0t)/(rtj**3)))*h # Iteracion de velocidad en x de jupiter
          
          y0t = y0t + vy0t*h # Iteracion de la posicion en x de la tierra
          y0j = y0j + vy0j*h # Iteracion de la posicion en x jupiter
          
          rt = np.sqrt(x0t**2 + y0t**2)
          rj = np.sqrt(x0j**2 + y0j**2)
          rtj = np.sqrt((x0t - x0j)**2 + (y0t - y0j)**2)
          
          t0 += h
          i += 1
          
          xgt.append(x0t)
          xgj.append(x0j)
          
          ygt.append(y0t)
          ygj.append(y0j)
          
          tg.append(t0)
     
#Variables------------------------------

x0t = 1        # Posicion incial en x de la Tierra
x0j = 5.20     # Posicion incial en x de Jupiter

vx0t = 0       # Velocidad incial en x de la Tierra
vx0j = 0       # Velocidad incial en x de Jupiter

vt = 29.78
vj = 13.07

ms = 1.98892e30     # Masa del Sol
mt = 5.9742e24      # Massa de la Tierra
mj = 1.8986e27      # Masa de Jupiter

y0t = 0        # Posicion incial en y de la Tierra
y0j = 0        # Posicion incial en y de Jupiter

vy0t = (2*np.pi)*(vt/29.78)   # Velocidad incial en y de la Tierra
vy0j = (2*np.pi)*(vj/29.78)   # Velocidad incial en y de Jupiter

t0 = 0                        # Tiempo inicial
tf = 11.89                    # Tiempo final
h = .001                      # Tamaños de paso
i = 0


# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0j,y0j,vx0j,vy0j,mj,ms,t0,tf,h)

# Grafica
N = f"fMetodo de Euler Cromer\nSistema Sol-Tierra-Luna\n"
plt.style.use("dark_background")
fig, ax = plt.subplots(facecolor = "blue")

# Funcion es para animacion, Bones y deslizadores
def update(i): # Funcion de la animacion
     ax.clear()
     color = ["yellow","green","red","white"]
     ax.set_title(N+r"$y$ vs $x$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     ax.grid(color = "turquoise")
     ax.axhline(color = "red")
     ax.axvline(color = "red")
     ax.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
     l1, = ax.plot(xgt[i],ygt[i],"o",color = "green", label = "Tierra",ms = 4)
     l2, = ax.plot(xgt[:i],ygt[:i],"--", color = "green",lw = .5, ms = 1)
     l3, = ax.plot(xgj[i],ygj[i],"o",color = "red", label = f"Jupiter",ms = 6)
     l4, = ax.plot(xgj[:i],ygj[:i],"--", color = "red",lw = .5, ms = 1)
     ax.plot(0,0,color = "black",label = f"Tiempo = {round(tg[i],3)}")
     ax.set_xlim(-11.62,11.62)
     ax.set_ylim(-5.32,5.32)
     ax.legend(edgecolor = "red", fontsize = 15, labelcolor = color)

def Iniciar(): # Funcion del boton Iniciar
     global ani 
     ani = animation.FuncAnimation(fig,update,range(0,len(xgj),117),interval = 0)
     canvas.draw()
     
def Pausar(): # Funcion del boton Pausar
     ani.event_source.stop()
     
def Reanudar(): # Funcion del boton Reanudar
     ani.event_source.start()

def Reset(): # Funcion del boton Reset
     ani.event_source.start()
     ani.event_source.stop()
     ax.clear()
     canvas.draw()

# Creacion de ventana
raiz = Tk()
raiz.title("Sistema Sol-Tierra-Jupiter")

wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()

raiz.geometry(str(wtotal-10)+"x"+str(htotal))
raiz.config(bg = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "Sistema Sol-Tierra-Jupiter, Problema de los 3 cuerpos")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usa el método de Euler Cromer para resolver el problema de los 3 cuerpos del Sistema Sol-Tierra-Jupiter.")

def Instrucciones():
     messagebox.showinfo("Instrucciones", "1.- Deslizar las barras y escoger los valores iniciales del ángulo y la velocidad del proyectil.\n\n2.- Pulse el botón “Iniciar”, se observará como inicia la animación, si desea pausar o reanudar la animación pulse los botones “Pausar” o “Reanudar”.\n\n3.- Si desea cambiar las condiciones iniciales del ángulo y la velocidad es recomendable que pulse el botón “Reset”, después deslice las barras e inicie la animación.\n\n4.- Si hay algún problema con la animación, pulsar dos veces el botón “Reset”, y inicie la animación de nuevo.\n\n5.- Es recomendable poner la pestaña en pantalla completa para una mejor visualización.")

def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la aplicacion?")
     if v == True:
          raiz.destroy()

# Menu
BarraMenu = Menu(raiz, bg = "blue", fg = "#03f943")
raiz.config(menu = BarraMenu, width = wtotal, height = htotal)

InformacionMenu = Menu(BarraMenu, tearoff = 0)
BarraMenu.add_cascade(label = "Información", menu = InformacionMenu)

InformacionMenu.add_command(label = "Acerca de...", command = InfoAcercaDe)
InformacionMenu.add_command(label = "Programa", command = InfoProducto)
InformacionMenu.add_command(label = "Descripcion", command = Descripcion)
InformacionMenu.add_command(label = "Instrucciones", command = Instrucciones)
InformacionMenu.add_command(label = "Salir", command = AccionSalir)

# Creacion del cuadro de la ventana o widget
frame = Frame(raiz)
frame.pack(fill = "both", expand = "True")
frame.config(bg = "blue")

# Colocacion de la grafica en el frame
canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack(padx = 5, pady = 5, fill = "both", expand = "True")

# Creacion de botones
BotonIniciar = Button(frame, text = "Iniciar", width = 30,height = 5, command = Iniciar)
BotonIniciar.pack(pady = 5, side = "left", expand = "True")
BotonIniciar.config(fg = "#03f943", bg = "black")

BotonPausar = Button(frame, text = "Pausar", width = 30,height = 5, command = Pausar)
BotonPausar.pack(pady = 5, side = "left", expand = "True")
BotonPausar.config(fg = "#03f943", bg = "black")

BotonReanudar = Button(frame, text = "Reanudar", width = 30,height = 5, command = Reanudar)
BotonReanudar.pack(pady = 5, side = "left", expand = "True")
BotonReanudar.config(fg = "#03f943", bg = "black")

BotonReset = Button(frame, text = "Reset", width = 30,height = 5, command = Reset)
BotonReset.pack(pady = 5, side = "left", expand = "True")
BotonReset.config(fg = "#03f943", bg = "black")

raiz.mainloop()