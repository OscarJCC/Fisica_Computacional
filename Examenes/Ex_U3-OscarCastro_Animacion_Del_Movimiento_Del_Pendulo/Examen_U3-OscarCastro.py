"""
Nombre: Examen Unidad 3 OscarCastro El Pendulo Simple
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
def Grados_A_Radianes(A0):
     return (A0*np.pi)/180

def Metodo_De_Euler(θ0,w0,t0,tf,h,l):
     global g, m, θg, tg, xg, yg
     θi = Grados_A_Radianes(θ0) 
     θg = [θi] # Lista para guardan las interaciones de θ(t) Euler
     tg = [t0] # Lista para guardar las interaciones del tiempo Euler

     while t0 < tf: # Metodo de Euler
          
          θi = θi + w0*h
          w0 = w0 - (g/l)*θi*h
          t0 += h
          
          θg.append(θi)
          tg.append(t0)

     xg = -l*np.sin(θg)
     yg = -l*np.cos(θg)
     
#Variables------------------------------

w0 = 0                       # Velocidad angular inicial
g = 9.81                     # Aceleracion de la gravedad
t0 = 0                       # Tiempo inicial
tf = 10                      # Tiempo final

#Condiciones Iniciales Modificacr Para La Animacion
θ0 = 11.5                    # Angulo inicial
l = 1                         # Longitud del pendulo
h = .001                     # Tamaños de paso


# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(θ0,w0,t0,tf,h,l)

# Criterio para marcar ejes de la grafica
if l <= 50:
     dx = l/100
     dy = l/50
elif l > 50:
     dx = l/10
     dy = l/5

# Grafica
N = f"El Péndulo Simple\n"
plt.style.use("dark_background")
fig, ax = plt.subplots(facecolor = "blue")#dpi = 110, figsize = (12.3,6.1), facecolor = "blue")

# Funcion es para animacion, Bones y deslizadores

def update(i): # Funcion de la animacion
     ax.clear()
     ax.set_title(N+fr"$y$ vs $x$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     #ax.grid(color = "turquoise")
     ax.axhline(color = "red")
     #ax.axvline(color = "red")
     ax.plot([0,xg[i]],[0,yg[i]], color = "red")
     ax.plot(xg[i],yg[i],"o", color = "yellow", label = f"Angulo = {θ0}°\nL   = {l} m\ntf  = {round(max(tg),3)} s\nθ   = {round(θg[i],3)}°\nt    = {round(tg[i],3)} s\nx   = {round(xg[i],3)} m\ny   = {round(yg[i],3)}",lw = 10)
     ax.plot(xg[:i],yg[:i],"--", color = "yellow",lw = .5, ms = 1)
     ax.set_xlim(-l,l)
     ax.set_ylim(-l-dy,0+dy)
     ax.legend(edgecolor = "red", fontsize = 15, labelcolor = "yellow")

# Primer deslizador
ax1 = plt.axes([.94,.1,.02,.8])  
Angulo = Slider(
     ax = ax1,
     label = "Angulo\ninicial",
     valmin = 1,
     valmax = 15,
     valinit = θ0,
     valstep = .5,
     orientation = "vertical",
     color = "yellow"
)

def Actualizax1(val): # Funcion del primer deslizador
     global θ0,l,dx,dy
     ax.clear()
     canvas.draw()
     Metodo_De_Euler(Angulo.val,w0,t0,tf,h,Longitud.val)
     θ0 = Angulo.val
     l = Longitud.val
     Iniciar
     fig.canvas.draw_idle()

Angulo.on_changed(Actualizax1)

# Segundo deslizador
ax2 = plt.axes([.04,.1,.02,.8])  
Longitud = Slider(
     ax = ax2,
     label = "Longitud\ninicial",
     valmin = 1,
     valmax = 10,
     valinit = l,
     valstep = 1,
     orientation = "vertical",
     color = "red"
)

def Actualizax2(val): # Funcion del segundo delizador
     global θ0,l,dx,dy
     ax.clear()
     canvas.draw()
     Metodo_De_Euler(Angulo.val,w0,t0,tf,h,Longitud.val)
     θ0 = Angulo.val
     l = Longitud.val
     if l <= 50:
          dx = l/100
          dy = l/50
     elif l > 50:
          dx = l/10
          dy = l/5
     Iniciar
     fig.canvas.draw_idle()

Longitud.on_changed(Actualizax2)

def Iniciar(): # Funcion del boton Iniciar
     global ani 
     ani = animation.FuncAnimation(fig,update,range(0,len(xg),l*10),interval = 0)
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
raiz.title("Examen Unidad 3 El Péndulo Simple ")

wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()

raiz.geometry(str(wtotal-10)+"x"+str(htotal))
raiz.config(bg = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "El Péndulo Simple , Aproximación Por Método De Euler")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usas el método de Euler para encontrar una aproximación a la solución de la ecuacion diferencial que modela el péndulo simple. Debido a que es una aproximación numérica la solución no es exacta.\n\nEcuaciones:\n\n\t\td^2θ       g\n\t               -------- = -----\n\t\tdt^2         L")

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