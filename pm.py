# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:45:06 2021

@author: Pushkino
"""

#Conversor Pulgadas a Metros
import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def in_m():
    global a
    a=cm.get()
    r=(a*2.54)/(100)
    mensaje = str(cm.get()) + " pulgadas equivalen a " + str(r) +" metros "
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
w2 = tk.Toplevel()
fondo=PhotoImage(file="caliper.gif")
lblimg=tk.Label(w2, image=fondo).place(x=0,y=0)
w2.geometry('460x310')
w2.title("Pulgadas a Metros")
#Obtención de datos en Centímetros
tk.Label(w2,text="Pulgadas a Metros").pack()
cm=tk.DoubleVar()
CM=tk.Entry(w2, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w2)
lblMensaje.pack()

btnCalcular=tk.Button(w2, text="Calcular", command=in_m).pack()

w2.mainloop()
