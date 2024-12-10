"""
Nombre: Examen Unidad 4 OscarCastro Sistema Sol-Tierra-Luna
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

def Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0l,y0l,vx0l,vy0l,ml,ms,t0,tf,h):
     global i, xgt, ygt, xgl, ygl, tg

     xgt = [x0t] # Matriz para guardan las interaciones de posicion en x tierra
     ygt = [y0t] # Matriz para guardan las interaciones de posicion en y tierra
     
     xgl = [x0l] # Matriz para guardan las interaciones de posicion en x de la Luna
     ygl = [y0l] # Matriz para guardan las interaciones de posicion en y de la Luna
     
     tg = [] # Matriz para guardar las interaciones de tiempo

     rts = np.sqrt(x0t**2 + y0t**2)                          # Radio sol tierra
     rls = np.sqrt(x0l**2 + y0l**2)                          # Radio sol Luna
     rtl = np.sqrt((x0t - x0l)**2 + (y0t - y0l)**2)    # Radio tierra Luna
     
     Cls = ml/ms
     Cts = mt/ms
     
     while t0 < tf: # Metodo de Euler

          vx0t = vx0t - 4*(np.pi**2)*(x0t/(rts**3) + (Cls)*((x0t-x0l)/(rtl**3)))*h # Iteracion de velocidad en x de la tierra
          vx0l = vx0l - 4*(np.pi**2)*(x0l/(rls**3) + (Cts)*((x0l-x0t)/(rtl**3)))*h # Iteracion de velocidad en x de la Luna
          
          x0t = x0t + vx0t*h # Iteracion de la posicion en x de la tierra
          x0l = x0l + vx0l*h # Iteracion de la posicion en x de la Luna

          vy0t = vy0t - 4*(np.pi**2)*(y0t/(rts**3) + (Cls)*((y0t-y0l)/(rtl**3)))*h # Iteracion de velocidad en x de la tierra
          vy0l = vy0l - 4*(np.pi**2)*(y0l/(rls**3) + (Cts)*((y0l-y0t)/(rtl**3)))*h # Iteracion de velocidad en x de la Luna
          
          y0t = y0t + vy0t*h # Iteracion de la posicion en x de la tierra
          y0l = y0l + vy0l*h # Iteracion de la posicion en x de la Luna
          
          rts = np.sqrt(x0t**2 + y0t**2)
          rls = np.sqrt(x0l**2 + y0l**2)
          rtl = np.sqrt((x0t - x0l)**2 + (y0t - y0l)**2)
          
          t0 += h
          
          xgt.append(x0t)
          xgl.append(x0l)
          
          ygt.append(y0t)
          ygl.append(y0l)
          
          tg.append(t0)   

#Variables------------------------------

x0t = 1                  # Posicion incial en x de la Tierra
x0l = x0t + 2.56267e-3     # Posicion incial en x de la Luna

vx0t = 0       # Velocidad incial en x de la Tierra
vx0l = 0       # Velocidad incial en x de la Luna

vt = 29.78
vl = vt + 1.022

ms = 1.98892e30     # Masa del Sol
mt = 5.9742e24      # Massa de la Tierra
ml = 7.349e22      # Masa de la Luna

y0t = 0        # Posicion incial en y de la Tierra
y0l = 0        # Posicion incial en y de la Luna

vy0t = (2*np.pi)*(vt/29.78)   # Velocidad incial en y de la Tierra
vy0l = (2*np.pi)*(vl/29.78)   # Velocidad incial en y de la Luna

t0 = 0                        # Tiempo inicial
tf = 1                    # Tiempo final
h = .0001                      # Tamaños de paso
j = 0

Metodo_De_Euler(x0t,y0t,vx0t,vy0t,mt,x0l,y0l,vx0l,vy0l,ml,ms,t0,tf,h)

# Grafica
N = f"Sistema Sol-Tierra-Luna"
plt.style.use("dark_background")
fig, ax = plt.subplots(facecolor = "blue")

# Funcion es para animacion, Bones y deslizadores
def update(i): # Funcion de la animacion
     global RadBot
     ax.clear()
     color = ["yellow","green","white"]
     ax.set_title(N+"\n"+r"$x$ vs $y$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     if RadBot.get() == 0:
          ax.plot(0,0,"o",color = "yellow", label = "Sol",ms = 10)
          ax.set_xlim(-2.35,2.35)
          ax.set_ylim(-1.1,1.1)
     elif RadBot.get() == 1:
          ax.plot([0,xgt[i-1]],[0,ygt[i-1]],"--",color = "yellow", label = "Dirección del Sol", ms = 1,lw = .5)
          ax.set_xlim(xgt[i]-.01,xgt[i]+.01)
          ax.set_ylim(ygt[i]-.005,ygt[i]+.005)
     ax.plot(xgt[i-1],ygt[i-1],"o",color = "green", label = "Tierra",ms = 6)
     ax.plot(xgl[i-1],ygl[i-1],"o",color = "white", label = "Luna",ms = 4)
     ax.plot(xgt[:i],ygt[:i],"--", color = "green",ms = 1,lw = 1)
     ax.plot(xgl[:i],ygl[:i],"--", color = "white",ms = 1,lw = 1)
     ax.plot(0,0, color = "black", label = f"t = {round(tg[i],2)}")
     ax.legend(edgecolor = "red", fontsize = 10)

def Iniciar(): # Funcion del boton Iniciar
     global ani 
     ani = animation.FuncAnimation(fig,update,range(0,len(xgt),50),interval = 0)
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
raiz.title("Sistema Sol-Tierra-Luna")

wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()

raiz.geometry(str(wtotal-10)+"x"+str(htotal))
raiz.config(bg = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "Sistema Sol-Tierra-Luna, Problema de los 3 cuerpos")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usa el método de Euler Cromer para resolver el problema de los 3 cuerpos del Sistema Sol-Tierra-Luna.")

def Instrucciones():
     messagebox.showinfo("Instrucciones", "1.- Pulse el botón “Iniciar”, se observará como inicia la animación, si desea pausar o reanudar la animación pulse los botones “Pausar” o “Reanudar”.\n\n2.- Si desea ver a la Tierra y a la Luna más de cerca presione el botón “Zoom Tierra-Luna” y si desea regresar a la vista normal presione el botón “Sol-Tierra-Luna”\n\n3- Si hay algún problema con la animación, pulsar dos veces el botón “Reset”, y inicie la animación de nuevo.")

def AccionSalir():
     v = messagebox.askokcancel("Salir", "¿Deseas salir de la animacion?")
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

# Variable para botones
RadBot = IntVar()

# Colocacion de la grafica en el frame
canvas = FigureCanvasTkAgg(fig, master = frame)
canvas.get_tk_widget().pack(padx = 5, pady = 5, fill = "both", expand = "True")

# Creacion de botones
BotonIniciar = Button(frame, text = "Iniciar", width = 30, border = 0 , height = 5 ,command = Iniciar)
BotonIniciar.pack(pady = 5, side = "left", expand = "True")
BotonIniciar.config(fg = "#03f943", bg = "black")

BotonPausar = Button(frame, text = "Pausar", width = 30, border = 0 , height = 5 ,command = Pausar)
BotonPausar.pack(pady = 5, side = "left", expand = "True")
BotonPausar.config(fg = "#03f943", bg = "black")

BotonReanudar = Button(frame, text = "Reanudar", width = 30, border = 0 , height = 5 ,command = Reanudar)
BotonReanudar.pack(pady = 5, side = "left", expand = "True")
BotonReanudar.config(fg = "#03f943", bg = "black")

BotonReset = Button(frame, text = "Reset", width = 30, border = 0 , height = 5 ,command = Reset)
BotonReset.pack(pady = 5, side = "left", expand = "True")
BotonReset.config(fg = "#03f943", bg = "black")

RBotonSTL = Radiobutton(frame, text = "Sol-Tierra-Luna", variable = RadBot, value = 0, width = 28, border = 0 , height = 5,)#, command = ZorNZ)
RBotonSTL.pack(pady = 5, side = "left", expand = "True")
RBotonSTL.config(fg = "#03f943", bg = "black")

RBotonZTL = Radiobutton(frame, text = "Zoom Tierra-Luna", variable = RadBot, value = 1, width = 28, border = 0 , height = 5,)#, command = ZorNZ)
RBotonZTL.pack(pady = 5, side = "left", expand = "True")
RBotonZTL.config(fg = "#03f943", bg = "black")

raiz.mainloop()