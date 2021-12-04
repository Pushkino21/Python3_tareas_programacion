# -*- coding: utf-8 -*-
"""
Spyder Editor

Daniel Michell Avila Garnica.
3°A Robotica
Multiconversor --Revisited
"""

import tkinter as tk   
from tkinter import PhotoImage
"""
Los bloques de funciones aqui declarados solo
llaman al programa un archivo.py
que contiene el conversor necesario
mas que por optimización de espacio
lo he realizado para no confundirme con
tanto codigo
"""
ventana = tk.Tk()
global Frm_conv

Frm_conv = tk.LabelFrame(ventana, text = 'Conversor seleccionado')

"""Bloque funciones para longitud """


def mtopg():
    """from mp import m_in
    m_in()""" #Remplace la anterior forma de invocar alas funciones individuales
    # por una donde se puedan mostrar y ocultar en la misma ventana, evitando asi el
    # error de eventos en las ventanas de tkinter invocadas en forma TopLevel
    
    def m_in():
        
        global a
        a=cm.get()
        r=(a*100)*(0.393701)
        mensaje = str(cm.get()) + " Metros equivalen a " + '\n'+str(r) +" pulgadas "
        lblMensaje.config(text=mensaje)
        return
    
    #apertura de Frame para albergar al conversor
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Metros a Pulgadas")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text="Calcular", command = m_in).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def intom():
    """from pm import in_m
    in_m()"""
    def in_m():
        global a
        a=cm.get()
        r=(a*2.54)/(100)
        mensaje = str(cm.get()) + " pulgadas equivalen a " +'\n'+str(r) +" metros "
        lblMensaje.config(text=mensaje)
        return
    #apertura de Frame para albergar al conversor
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Pulgadas a metros")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text="Calcular", command =in_m).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
    
def cmtopg():
    """from cp import cm_in
    cm_in()"""
    
    def cm_in():
        global a
        a=cm.get()
        r=a*0.393701
        mensaje = str(cm.get()) + " centímetros equivalen a " +'\n'+ str(r) +" pulgadas "
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Centimetros a Pulgadas")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text="Calcular", command = cm_in).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def intocm():
    """from pc import in_cm
    in_cm()"""
    
    def in_cm():
        global a
        a=cm.get()
        r=a*2.54
        mensaje = str(cm.get()) + " pulgadas equivalen a " +'\n'+ str(r) +" centimetros "
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Pulgadas a Centimetros")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = in_cm).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return    

#final del blloque de funciones para longitud
"""Bloque funciones para temperatura"""

def CtoF():
    """from CF import C_F
    C_F()"""
    def C_F():
        global a
        a=cm.get()
        r=(a*(float(9/5)))+32
        mensaje = str(cm.get())+"°" + " centigrados equivalen a " +'\n'+ str(r) +"°"+" farenheit"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Celsius a Fahrenheit")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = C_F).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def FtoC():
    """from FC import in_m
    in_m()"""
    
    def F_C():
        global a
        a=cm.get()
        r=(a-32)*(float(5/9))
        mensaje = str(cm.get())+"°" + " Fahrenheit equivalen a " +'\n'+ str(r) +"°"+" Centigrados"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Fahrenheit a Celsius")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = F_C).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
   
    
"""Bloque funciones para tiempo"""
   
def Htom():
    """from HM import H_M
    H_M()"""
    
    def H_M():
        global a
        a=cm.get()
        r=a*60
        mensaje = str(cm.get())+" horas equivalen a " +'\n'+ str(r) +" Minutos"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Horas a Minutos")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = H_M).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def Htos():
    """from HS import H_s
    H_s()"""
    
    def H_S():
        global a
        a=cm.get()
        r=a*3600
        mensaje = str(cm.get())+" horas equivalen a " +'\n'+ str(r) +" Segundos"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Horas a segundos")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = H_S).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return


def Mtos():
    """from MS import M_S
    M_S()"""
    
    def M_S():
        global a
        a=cm.get()
        r=a*60
        mensaje = str(cm.get())+" minutos equivalen a " +'\n'+ str(r) +" segundos"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Minutos a Segundos")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = M_S).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
    
"""Bloque funciones para Velocidad"""

def khtoMs():
    """from KM import K_M
    K_M()"""
    
    def K_M():
        global a
        a=cm.get()
        r=a/3.6
        mensaje = str(cm.get())+" km/h equivalen a " +'\n'+ str(r) +" m/s"
        lblMensaje.config(text=mensaje)
        return

    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Kilometros/h a Metros/s")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = K_M).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
    
def khtoMis():
    """from KMI import K_Mi
    K_Mi()"""
    
    def K_Mi():
        global a
        a=cm.get()
        r=a/1.609
        mensaje = str(cm.get())+" km/h equivalen a " +'\n'+ str(r) +" mi/H"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "Kilometros/h a Millas/h")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = K_Mi).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
    
""" Bloque funciones para presion """    
def PSIBAR():
    """from PB import PB
    PB()"""
    
    def PB():
        global a
        a=cm.get()
        r=a/14.504
        mensaje = str(cm.get())+" PSI equivalen a " +'\n'+ str(r) +" Bar"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "PSI a BAR")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = PB).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def PSIPASC():
    """from PSP import PP
    PP()"""
    
    def PP():
        global a
        a=cm.get()
        r=a*6894.757
        mensaje = str(cm.get())+" PSI equivalen a " +'\n'+ str(r) +" Pascales"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "PSI a Pascales")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = PP).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return

def BARPASC():
    """from BP import BP
    BP()"""
    
    def BP():
        global a
        a=cm.get()
        r=a*100000
        mensaje = str(cm.get())+" Bar equivalen a " +'\n'+ str(r) +" Pascales"
        lblMensaje.config(text=mensaje)
        return
    
    frm_MTOPG = tk.LabelFrame(Frm_conv,text = "BAR a Pascales")
    
    cm=tk.DoubleVar()
    CM=tk.Entry(frm_MTOPG, textvariable=cm).pack(expand = True, fill = 'both', side = 'left')
    
    #Bloque mensaje
    lblMensaje = tk.Label(frm_MTOPG, text = 'resultado se imprimirá\n en breve')
    lblMensaje.pack(expand = True, fill = 'both', side = 'bottom')

    btnCalcular=tk.Button(frm_MTOPG, text = "Calcular", command = BP).pack(expand = True, fill = 'both', side = 'right')
    btnsu_1 = tk.Button(frm_MTOPG, text = 'Ocultar', command = frm_MTOPG.destroy)
    btnsu_1.pack(expand = True, fill = 'both', side = 'bottom')
    frm_MTOPG.pack(expand = True, fill = 'both')
    return
    
   


#imagen fondo ventana
#fondo=PhotoImage(file="engrane.gif")
#lblimg=tk.Label(ventana, image=fondo).place(x=-250,y=-100)

#geometria de la ventana
ventana.geometry('800x600')
ventana.config(bg='blue')
#Nombre de la ventana
ventana.title('Multi conversor de unidades')

#Frame de primeros conversores
frm_1row = tk.LabelFrame(ventana)
"""Agregar objetos al frame Longitudes"""
framelong = tk.LabelFrame(frm_1row , text="Conversiones Longitudes")
#fnd = PhotoImage(file="speedometer.gif")

frm_mts_inc = tk.LabelFrame(framelong, text = 'Metros a Pulgadas')

#lblfnd = tk.Label(frm_mts_inc, image=fnd).place(x=0,y=0)

btn1 = tk.Button(frm_mts_inc, text = 'Abrir', command = mtopg, activebackground = '#78d6ff')
btn1.pack(expand = True, fill = 'both', side = 'left')


frm_mts_inc.pack(expand = True, fill = 'both')

frm_inc_mts = tk.LabelFrame(framelong, text =  'Pulgadas a Metros')

lbintom = tk.Label(frm_inc_mts, text = "Pulgadas a Metros")
lbintom.pack(expand = True, fill = 'both', side = 'left')

btn2 = tk.Button(frm_inc_mts,text = 'Abrir', command = intom, activebackground = '#78d6ff')
btn2.pack(expand = True, fill = 'both', side = 'left')

frm_inc_mts.pack(expand = True, fill = 'both')

frm_cm_inc = tk.LabelFrame(framelong, text = 'Centimetros a Pulgadas')

lbcmtoin = tk.Label(frm_cm_inc, text = "Centimetros a Pulgadas")
lbcmtoin.pack(expand = True, fill = 'both', side = 'left')

btn3 = tk.Button(frm_cm_inc,text = 'Abrir', command = cmtopg, activebackground = '#78d6ff')
btn3.pack(expand = True, fill = 'both', side = 'left')

frm_cm_inc.pack(expand = True, fill = 'both')

frm_inc_cm = tk.LabelFrame(framelong, text = 'Pulgadas a Centimetros')

lbintocm = tk.Label(frm_inc_cm, text = "Pulgadas a Centimetros")
lbintocm.pack(expand = True, fill = 'both', side = 'left')

btn4 = tk.Button(frm_inc_cm,text = 'Abrir', command = intocm, activebackground = '#78d6ff')
btn4.pack(expand = True, fill = 'both', side = 'left')

frm_inc_cm.pack(expand = True, fill = 'both')

framelong.pack(expand = True, fill = 'both', side = 'left')


"""Frame de opciones temperatura"""

frametemp = tk.LabelFrame(frm_1row , text="Conversiones Temperaturas")

frm_C_F = tk.LabelFrame(frametemp, text = 'Celsius a Fahrenheit')

lbCF = tk.Label(frm_C_F, text = "Celsius a Fahrenheit")
lbCF.pack(expand = True, fill = 'both', side = 'left')

btn5 = tk.Button(frm_C_F,text = 'Abrir', command = CtoF, activebackground = '#78d6ff')
btn5.pack(expand = True, fill = 'both', side = 'left')

frm_C_F.pack(expand = True, fill = 'both')

frm_F_C = tk.LabelFrame(frametemp, text = 'Fahrenheit a Celsius')

lbFC = tk.Label(frm_F_C, text = "Fahrenheit a Celsius")
lbFC.pack(expand = True, fill = 'both', side = 'left')

btn6 = tk.Button(frm_F_C, text = 'Abrir', command = FtoC, activebackground = '#78d6ff')
btn6.pack(expand = True, fill = 'both', side = 'left')
frm_F_C.pack(expand = True, fill = 'both')

frametemp.pack(expand = True, fill = 'both', side = 'right')

frm_1row.pack(expand = True, fill = 'both', side = 'left')



Frm_conv = tk.LabelFrame(ventana, text = 'Conversor seleccionado')

Frm_conv.pack(expand = True, fill = 'both', side = 'right')



frm_2row = tk.LabelFrame(ventana, text = 'fila dos')

#Frame de opciones tiempo
frametime = tk.LabelFrame(frm_2row, text="Conversiones Tiempo")

frm_HH_MM = tk.LabelFrame(frametime, text = 'Horas a Minutos')

lbHM = tk.Label(frm_HH_MM, text = "Horas a Minutos")
lbHM.pack(expand = True, fill = 'both', side = 'left')

btn7 = tk.Button(frm_HH_MM,text = 'Abrir', command = Htom, activebackground = '#78d6ff')
btn7.pack(expand = True, fill = 'both', side = 'left')

frm_HH_MM.pack(expand = True, fill = 'both')

frm_HH_SS = tk.LabelFrame(frametime, text = 'Horas a segundos')

lbHS = tk.Label(frm_HH_SS , text = "Horas a Segundos")
lbHS.pack(expand = True, fill = 'both', side = 'left')

btn8 = tk.Button(frm_HH_SS,text = 'Abrir', command = Htos, activebackground = '#78d6ff')
btn8.pack(expand = True, fill = 'both', side = 'left')

frm_HH_SS.pack(expand = True, fill = 'both')

frm_MM_SS = tk.LabelFrame(frametime, text = 'Minutos a Segundos')

lbMS = tk.Label(frm_MM_SS, text = "Minutos a Segundos")
lbMS.pack(expand = True, fill = 'both', side = 'left')

btn9 = tk.Button(frm_MM_SS,text = 'Abrir', command = Mtos, activebackground = '#78d6ff')
btn9.pack(expand = True, fill = 'both', side = 'left')

frm_MM_SS.pack(expand = True, fill = 'both')

frametime.pack(expand = True, fill = 'both', side = 'bottom')

#Frame de opciones Velocidad
framevel = tk.LabelFrame(frm_2row, text="Conversiones Velocidades")

frm_KM_H_M_S = tk.LabelFrame(framevel, text = ' Kilometros/h a M/s')

lbkm = tk.Label(frm_KM_H_M_S, text = "Kilometros hora a metros segundo")
lbkm.pack(expand = True, fill = 'both', side = 'left')

btn10 = tk.Button(frm_KM_H_M_S,text = 'Abrir', command = khtoMs, activebackground = '#78d6ff')
btn10.pack(expand = True, fill = 'both', side = 'left')

frm_KM_H_M_S.pack(expand = True, fill = 'both')

frm_K_MI = tk.LabelFrame(framevel, text = 'Kilometros/h a Millas/h')

lbkmi = tk.Label(frm_K_MI, text = "Kilometros hora a millas hora")
lbkmi.pack(expand = True, fill = 'both', side = 'left')

btn11 = tk.Button(frm_K_MI,text = 'Abrir', command = khtoMis, activebackground = '#78d6ff')
btn11.pack(expand = True, fill = 'both', side = 'left')

frm_K_MI.pack(expand = True, fill = 'both')

framevel.pack(expand = True, fill = 'both', side = 'bottom')

#Frame de opciones Presion
framepre = tk.LabelFrame(frm_2row, text="Conversiones Presiones")

frm_PSI_BAR = tk.LabelFrame(framepre, text = 'PSI a BAR')

lbpb = tk.Label(frm_PSI_BAR, text = "PSI a Bares")
lbpb.pack(expand = True, fill = 'both', side = 'left')

btn12 = tk.Button(frm_PSI_BAR,text = 'Abrir', command = PSIBAR, activebackground = '#78d6ff')
btn12.pack(expand = True, fill = 'both', side = 'left')

frm_PSI_BAR.pack(expand = True, fill = 'both')

frm_PSI_PSC = tk.LabelFrame(framepre, text = 'PSI a PASCALES')

lbpp = tk.Label(frm_PSI_PSC, text = "PSI a Pascales")
lbpp.pack(expand = True, fill = 'both', side = 'left')

btn13 = tk.Button(frm_PSI_PSC,text = 'Abrir', command = PSIPASC, activebackground = '#78d6ff')
btn13.pack(expand = True, fill = 'both', side = 'left')

frm_PSI_PSC.pack(expand = True, fill = 'both')


frm_BAR_PSC = tk.LabelFrame(framepre, text = 'Bares a Pascales')

lbbp = tk.Label(frm_BAR_PSC, text = "Bares a Pascales")
lbbp.pack(expand = True, fill = 'both', side = 'left')

btn14 = tk.Button(frm_BAR_PSC,text = 'Abrir', command = BARPASC, activebackground = '#78d6ff')
btn14.pack(expand = True, fill = 'both', side = 'left')

frm_BAR_PSC.pack(expand = True, fill = 'both', side = 'left')

framepre.pack(expand = True, fill = 'both', side = 'bottom')
frm_2row.pack(expand = True, fill = 'both', side = 'bottom')

ventana.mainloop()