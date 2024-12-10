"""
Nombre: Examen Unidad 2 OscarCastro Movimiento De Proyectiles Caso Ideal
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

def Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h):
     global i, j, g, xg, yg, tg, vg, v
     
     tf = 100000000
     vx0 = v0*np.cos(Grados_A_Radianes(A0)) # Velocidad inicial en direccion x
     vy0 = v0*np.sin(Grados_A_Radianes(A0)) # Velocidad inicial en direccion y
     v = np.sqrt(vx0**2+vy0**2)
     xg = [x0]   # Lista para guardar las interaciones de x(t)
     yg = [y0]   # Lista para guardar las interaciones de y(t)
     tg = [t0]   # Lista para guardar las interaciones del tiempo
     vg = [v]
     
     while t0 < tf: # Metodo de Euler
          vx0 = vx0
          x0 = x0 + vx0*h
          vy0 = vy0 - g*h
          y0 = y0 + vy0*h
          t0 += h
          v = np.sqrt(vx0**2+vy0**2)
          xg.append(x0)
          yg.append(y0)
          tg.append(t0)
          vg.append(v)

          if y0 < 0: # Criterio de paro cuando el proyectil cae
               tf = t0
     
#Variables------------------------------

x0 = 0    # Posicion inicial
y0 = 0    # Altura inicial
t0 = 0    # Tiempo inicial
tf = 0
g = 9.81  # Aceleracion de la gravedad

# Condiciones Iniciales Modificar Para La Animacion
A0 = 85   # Angulo Inicial
v0 = 700    # Velocidad inicial
h = .001   # Tamaño de paso

# Aplicacion del Metodo de Euler para encontrar la solucion numerica de las Ec. Dif.
Metodo_De_Euler(x0,y0,v0,t0,tf,A0,h)

# Criterio para marcar ejes de la grafica
if v0 <= 50:
     dx = v0/100
     dy = v0/50
elif v0 > 50:
     dx = v0/10
     dy = v0/5

# Grafica
N = f"Movimiento De Proyectiles Caso Ideal\n"
plt.style.use("dark_background")
fig, ax = plt.subplots(facecolor = "blue")#dpi = 110, figsize = (12.3,6.1), facecolor = "blue")

# Funcion es para animacion, Bones y deslizadores

def update(i): # Funcion de la animacion
     ax.clear()
     ax.set_title(N+fr"$y$ vs $x$", fontsize = 15)
     ax.set_xlabel(r"$x(t)$")
     ax.set_ylabel(r"$y(t)$")
     ax.grid(color = "turquoise")
     ax.axhline(color = "red")
     ax.axvline(color = "red")
     l1, = ax.plot(xg[i],yg[i],"o", color = "yellow",
             label = f"Angulo = {A0}°\nvi = {v0} m/s\ntf = {round(max(tg),3)} s\nv   = {round(vg[i],3)} m/s\nt  = {round(tg[i],3)} s\nx  = {round(xg[i],3)} m\ny  = {round(yg[i],3)} m")
     l2, = ax.plot(xg[:i],yg[:i],"--", color = "yellow", lw = .5, ms = 1)
     ax.set_xlim(min(xg)-dx,max(xg)+dx)
     ax.set_ylim(min(yg)-dy,max(yg)+dy)
     ax.legend(edgecolor = "red", fontsize = 15, labelcolor = "yellow")

# Primer deslizador
ax1 = plt.axes([.94,.1,.02,.8])  
Angulo = Slider(
     ax = ax1,
     label = "Angulo\ninicial",
     valmin = 10,
     valmax = 85,
     valinit = A0,
     valstep = 5,
     orientation = "vertical",
     color = "yellow"
)

def Actualizax1(val): # Funcion del primer deslizador
     global A0, v0
     ax.clear()
     canvas.draw()
     Metodo_De_Euler(x0,y0,Velocidad.val,t0,tf,Angulo.val,h)
     A0 = Angulo.val
     v0 = Velocidad.val
     Iniciar
     fig.canvas.draw_idle()

Angulo.on_changed(Actualizax1)

# Segundo deslizador
ax2 = plt.axes([.04,.1,.02,.8])  
Velocidad = Slider(
     ax = ax2,
     label = "Velocidad\ninicial",
     valmin = 10,
     valmax = 700,
     valinit = v0,
     valstep = 5,
     orientation = "vertical",
     color = "red"
)

def Actualizax2(val): # Funcion del segundo delizador
     global A0, v0,dx,dy
     ax.clear()
     canvas.draw()
     Metodo_De_Euler(x0,y0,Velocidad.val,t0,tf,Angulo.val,h)
     A0 = Angulo.val
     v0 = Velocidad.val
     if v0 <= 50:
          dx = v0/100
          dy = v0/50
     elif v0 > 50:
          dx = v0/10
          dy = v0/5
     Iniciar
     fig.canvas.draw_idle()

Velocidad.on_changed(Actualizax2)

def Iniciar(): # Funcion del boton Iniciar
     global ani 
     ani = animation.FuncAnimation(fig,update,range(0,len(xg),v0*5),interval = 0)
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
raiz.title("Examen Unidad 2 Movimiento De Proyectiles Caso Ideal")

wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()

raiz.geometry(str(wtotal-10)+"x"+str(htotal))
raiz.config(bg = "blue")

#Funciones de Menu o de ventanas emergentes
def InfoAcercaDe():
     messagebox.showinfo("Creador", "Oscar Joel Castro Contreras\n------ Ingeniero Físico -------\n----------  UA de C  -----------")

def InfoProducto():
     messagebox.showinfo("Programa", "Movimiento De Proyectiles Caso Ideal, Aproximación Por Método De Euler")

def Descripcion():
     messagebox.showinfo("Descripción", "Este programa usas el método de Euler para encontrar una aproximación a la solución de las ecuaciones diferenciales que modelan el movimiento de un proyectil como un caso ideal, es decir, sin considerar fuerzas de arrastre. Debido a que es una aproximación numérica la solución no es exacta.\n\nEcuaciones:\n\n\t\td^2x             d^2y\n\t               -------- = 0    -------- = -g\n\t\tdt^2             dt^2")

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