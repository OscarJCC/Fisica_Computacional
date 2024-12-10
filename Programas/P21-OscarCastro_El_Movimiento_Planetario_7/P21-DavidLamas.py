#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import plotly.graph_objects as pgo

# Constantes
a = 0.39 # Semieje mayor de la órbita de Mercurio (UA)
e = 0.206 # Excentricidad de la órbita de Mercurio
v0 = np.sqrt(4*np.pi**2 *(1+e)/(a*(1-e))) # Velocidad inicial de Mercurio

# Condiciones iniciales
x0 = a*(1-e) # Posición inicial en x (UA)
y0 = 0 # Posición inicial en y (UA)
vx0 = 0 # Velocidad inicial en x (UA/año)
vy0 = v0 # Velocidad inicial en y (UA/año)
ti = 0  #Tiempo inicial (s)
h = 1e-3 # Paso de tiempo

# Condiciones iniciales
x, y = [x0], [y0]
vx, vy = [vx0], [vy0]

# Método de Euler-Cromer
while ti <= 2:
    r = np.sqrt(x0**2 + y0**2) # Distancia al Sol
    vx0 = vx0 - (4*np.pi**2 *x0/r**3)*h # Velocidad en x
    vy0 = vy0 - (4*np.pi**2 *y0/r**3)*h # Velocidad en y
    x0 = x0 + vx0*h # Posición en x
    x.append(x0)
    y0 = y0 + vy0*h # Posición en y
    y.append(y0)
    ti += h

fig = pgo.Figure()
fig.add_traces(pgo.Scatter(x=x, y=y, name="Órbita Mercurio", line=dict(color="#ddd")))
fig.add_traces(pgo.Scatter(x=[x[-1]], y=[y[-1]], mode='markers', marker=dict(size=5, color='#ddd'), name='Mercurio'))
fig.add_traces(pgo.Scatter(x=[0], y=[0], name="Sol", mode='markers', marker=dict(size=35, color='yellow')))
fig.update_layout(title = "Movimiento de Mercurio alrededor del Sol.",
plot_bgcolor='#141a16',
width=600, height=500,
xaxis_range=[min(x)-0.1, max(x)+0.1], yaxis_range=[min(y)-0.1, max(y)+0.1],
xaxis=dict(showgrid=False),
yaxis=dict(showgrid=False),
xaxis_title = "x (UA)", yaxis_title = "y (UA)")
fig.show()


# In[ ]:




