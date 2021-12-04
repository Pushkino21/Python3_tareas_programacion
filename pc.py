# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 21:57:41 2021

@author: Pushkino
"""
#conversor pulgadas a cm
import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def in_cm():
    global a
    a=cm.get()
    r=a*2.54
    mensaje = str(cm.get()) + " pulgadas equivalen a " + str(r) +" centimetros "
    lblMensaje.config(text=mensaje)
    return

#Creación del widget ventana
w2 = tk.Toplevel()
fondo=PhotoImage(file="caliper.gif")
lblimg=tk.Label(w2, image=fondo).place(x=0,y=0)

w2.geometry('460x310')
w2.title("Pulgadas a Centimetros")
#Obtención de datos en Centímetros
tk.Label(w2,text="Pulgadas a Centimetros").pack()
cm=tk.DoubleVar()
CM=tk.Entry(w2, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w2)
lblMensaje.pack()

btnCalcular=tk.Button(w2, text="Calcular", command=in_cm).pack()

w2.mainloop()