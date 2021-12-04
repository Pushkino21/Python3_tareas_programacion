# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:19:19 2021

@author: Pushkino
"""

import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def K_M():
    global a
    a=cm.get()
    r=a/3.6
    mensaje = str(cm.get())+" km/h equivalen a " + str(r) +" m/s"
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
w1 = tk.Toplevel()
fondo=PhotoImage(file="vel.gif")
lblimg=tk.Label(w1, image=fondo).place(x=0,y=0)

w1.geometry('460x310')
w1.title("KM/H a M/S")
#Obtención de datos en Centímetros
tk.Label(w1,text="Kilometro Hora a Metro segundo", padx=10,pady=10, ).pack()
cm=tk.DoubleVar()
CM=tk.Entry(w1, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w1)
lblMensaje.pack()

btnCalcular=tk.Button(w1, text="Calcular", command=K_M).pack()
c_v = tk.Button(w1, text = "Cerrar", command=w1.destroy).pack()
w1.mainloop()