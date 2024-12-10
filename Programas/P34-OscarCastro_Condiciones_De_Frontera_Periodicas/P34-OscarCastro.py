"""
Nombre: P34-OscarCastro Condiciones De Frontera Periodicas
Fecha Inicio:
Fecha Final:
Autor: Oscar Joel Castro Contreras
Descripcion:

"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt
import time

# Funciones------------------------------
def mod(x,l):
     return x - l*np.round(x/l)

def ejercicio_1(xg,lg):
     texto = """\n\n1.- Una forma de calcular la posición de una partícula es mediante el uso del operador módulo, %. Por ejemplo,\n17 % 5 es igual a 2, ya que 17 dividido por 5 arroja un resto (remanente, residuo) de 2. El operador % también\nse puede usar con números de punto flotante. Por ejemplo, 10.2 % 5 = 0.2.\nEscribe un pequeño programa de prueba para ver cómo funciona la función % y determina el resultado de:\n"""
     m = [xg%lg,-xg%lg-lg,xg%-lg+lg,-xg%-lg]
     inciso = ["a) 10.2 % 3.3   = ","b) -10.2 % 3.3  = ","c) 10.2 % -3.3  = ","d) -10.2 % -3.3 = "]
     
     print(texto)
     
     for i in range(len(m)):
          print(inciso[i] + f"{m[i]}")
          

def ejercicio_2(xg,lg):
     texto = """\n\n2.- De los resultados del ejercicio anterior (1), se puede considerar escribir x = x % L como alternativa al\ncálculo de la distancia mediante una sentencia con if-else. ¿Qué hay al respecto de valores negativos de x? En\neste caso, -17 % 5 = -2. Como queremos que la posición resultante sea positiva, podríamos escribir: si x < 0,\nhacer x % L + L de lo contrario, hacer x % L.\nVerifica que esto funcione como se pretende.\n"""
     print(texto)
     
     x = [xg,-xg,xg,-xg]
     l = [lg,lg,-lg,-lg]
     m = [xg%lg,-xg%lg,xg%-lg,-xg%-lg]
     inciso = ["a) 10.2 % 3.3   = ","b) -10.2 % 3.3  = ","c) 10.2 % -3.3  = ","d) -10.2 % -3.3 = "]
     
     for i in range(len(m)):
          if x[i] < 0 and l[i] > 0:
               m[i] = m[i] - lg
          elif x[i] > 0 and l[i] < 0:
               m[i] = m[i] + lg
          else:
               m[i] = m[i]
     
     for i in range(len(m)):
          print(inciso[i] + f"{m[i]}")
          
     print("\nResiduo\n-17 % 5 =",-17%-+5)
     print("\nResiduo con la condicion aplicada\n-17 % 5 =",mod(-17,5))
     
     texto1 = """\nVemos que hacer este analisis de si x > 0 o x < 0 no funciona muy bien ya que al calcular el residuo directo\nsin la funcion modulo este solo sale negativo cuando el divisor o el dividendo son negativos pero en el caso\nen el que el dividendo y divisor son negativos juntos el residuo es positivo por lo que al aplicar las\ncondiciones en este caso no sale el mismo resultado que con la funcion modulo de python."""
     print(texto1)

def ejercicio_3(xg,lg):
     texto = """\n3.- En este contexto, escribe un pequeño programa para determinar si el operador % es más rápido que la\nsentencia if-else."""
     print(texto)
     
     ti1 = time.time()
     
     x = [xg,-xg,xg,-xg]
     l = [lg,lg,-lg,-lg]
     m = [xg%lg,-xg%lg,xg%-lg,-xg%-lg]
     
     for i in range(len(m)):
          if x[i] < 0 and l[i] > 0:
               m[i] = m[i] - lg
          elif x[i] > 0 and l[i] < 0:
               m[i] = m[i] + lg
          else:
               m[i] = m[i]
               
     tf1 = time.time()
     
     ti2 = time.time()
     
     m = [xg%lg,-xg%lg-lg,xg%-lg+lg,-xg%-lg]
     
     tf2 = time.time()
     
     print("\nUsando la sentencia if-else tardo: ",tf1-ti1)
     print("\nUsando la funcion % tardo: ",tf2-ti2)
     
     print("\nVemos que es intantaneo el calculo en los 2 casos.")
# Variables------------------------------
xg = 10.2
lg = 3.3

ejercicio_1(xg,lg)

ejercicio_2(xg,lg)

ejercicio_3(xg,lg)