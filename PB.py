# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 01:54:10 2021

@author: Pushkino
"""

import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def PB():
    global a
    a=cm.get()
    r=a/14.504
    mensaje = str(cm.get())+" PSI equivalen a " + str(r) +" Bar"
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
w1 = tk.Toplevel()
fondo=PhotoImage(file="pre.gif")
lblimg=tk.Label(w1, image=fondo).place(x=0,y=0)

w1.geometry('460x310')
w1.title("PSI a BAR")
#Obtención de datos en Centímetros
tk.Label(w1,text="Libra por pulgada^2 a Bar", padx=10,pady=10, ).pack()
cm=tk.DoubleVar()
CM=tk.Entry(w1, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w1)
lblMensaje.pack()

btnCalcular=tk.Button(w1, text="Calcular", command=PB).pack()
c_v = tk.Button(w1, text = "Cerrar", command=w1.destroy).pack()
w1.mainloop()