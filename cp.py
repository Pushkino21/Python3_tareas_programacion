# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:27:16 2021

@author: Pushkino
"""
#Conversor centimetros a pulgadas
import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def cm_in():
    global a
    a=cm.get()
    r=a*0.393701
    mensaje = str(cm.get()) + " centímetros equivalen a " + str(r) +" pulgadas "
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
w1 = tk.Toplevel()
fondo=PhotoImage(file="caliper.gif")
lblimg=tk.Label(w1, image=fondo).place(x=0,y=0)

w1.geometry('460x310')
w1.title("Centimetros a Pulgadas")
#Obtención de datos en Centímetros
tk.Label(w1,text="Centímetros a  Pulgadas", padx=40,pady=40, ).pack()
cm=tk.DoubleVar()
CM=tk.Entry(w1, textvariable=cm).pack()


#Bloque mensaje
lblMensaje = tk.Label(w1)
lblMensaje.pack()

btnCalcular=tk.Button(w1, text="Calcular", command=cm_in).pack()
c_v = tk.Button(w1, text = "Cerrar", command=w1.destroy).pack()
w1.mainloop()
