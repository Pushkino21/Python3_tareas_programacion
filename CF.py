# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 00:00:38 2021

@author: Pushkino
"""

import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def C_F():
    global a
    a=cm.get()
    r=(a*(float(9/5)))+32
    mensaje = str(cm.get())+"°" + " centigrados equivalen a " + str(r) +"°"+" farenheit"
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
w1 = tk.Toplevel()
fondo=PhotoImage(file="temp.gif")
lblimg=tk.Label(w1, image=fondo).place(x=0,y=0)

w1.geometry('460x310')
w1.title("Celsius a Fahrenheit")
#Obtención de datos en Centímetros
tk.Label(w1,text="Celsius a Fahrenheit", padx=10,pady=10, ).pack()
cm=tk.DoubleVar()
CM=tk.Entry(w1, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w1)
lblMensaje.pack()

btnCalcular=tk.Button(w1, text="Calcular", command=C_F).pack()
c_v = tk.Button(w1, text = "Cerrar", command=w1.destroy).pack()
w1.mainloop()