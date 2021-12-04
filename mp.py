# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 22:28:40 2021

@author: Pushkino
"""
#Conversor metros a Pulgadas
import tkinter as tk
from tkinter import PhotoImage
#from tkinter import messagebox
def m_in():
    global a
    a=cm.get()
    r=(a*100)*(0.393701)
    mensaje = str(cm.get()) + " Metros equivalen a " + str(r) +" pulgadas "
    lblMensaje.config(text=mensaje)
    return
#Creación del widget ventana
#w2 = tk.Toplevel()
fondo=PhotoImage(file="caliper.gif")
lblimg=tk.Label(Frm_conv, image=fondo).place(x=0,y=0)
#w2.geometry('460x310')
#w2.title("Metros a Pulgadas")
#Obtención de datos en Centímetros
tk.Label(Frm_conv,text="Metros a Pulgadas").pack()
cm=tk.DoubleVar()
CM=tk.Entry(Frm_conv, textvariable=cm).pack(expand = True, fill = 'both')


#Bloque mensaje
lblMensaje = tk.Label(Frm_conv)
lblMensaje.pack(expand = True, fill = 'both')

btnCalcular=tk.Button(Frm_conv, text="Calcular", command=m_in).pack(expand = True, fill = 'both')

#w2.mainloop()

