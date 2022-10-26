#Import´s
from cProfile import label
from msilib.schema import File
from statistics import geometric_mean
from tkinter import *
from tokenize import String
from unittest import result
from matplotlib.pyplot import text
from numpy import size
import cv2

from setuptools import Command

puntos = 0

#FUNCIONES
def buena():
    global puntos
    puntos=puntos + 1

def pregunta1():
    label_Title.destroy()
    campo_Nombre.destroy()
    botonJugar.destroy()
    entry1.destroy()

    #
    No_pregunta = Label(ventana,text=' PREGUNTA No. 1',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que significan las siglas CMMI?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Compatibility Maturity Model Internal',relief=FLAT,font=('Arial',30))
    opc1.place(x=550,y=200)
    opc2=Label(ventana,text='B) Capability Maturity Model Integration',relief=FLAT,font=('Arial',30))
    opc2.place(x=550,y=300)
    opc3=Label(ventana,text='C) Compatibility Maturity Model Internal',relief=FLAT,font=('Arial',30))
    opc3.place(x=550,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta2(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        buena(),
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta2(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta2(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta2():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 2',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Cuantos niveles conforman el CMMI?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen2)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) 5 Niveles',relief=FLAT,font=('Arial',30))
    opc1.place(x=750,y=200)
    opc2=Label(ventana,text='B) 3 Niveles',relief=FLAT,font=('Arial',30))
    opc2.place(x=750,y=300)
    opc3=Label(ventana,text='C) 6 Niveles',relief=FLAT,font=('Arial',30))
    opc3.place(x=750,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        buena(),
        opc2.destroy(),
        pregunta3(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta3(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta3(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta3():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 3',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='Es el proceso que se encarga de mejorar continuamente los procesos',font=('Arial',30),bg='peach puff')
    pregunta.place(x=200,y=100)
    label_imagen =  Label(ventana, image = imagen3)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Optimización',relief=FLAT,font=('Arial',30))
    opc1.place(x=650,y=200)
    opc2=Label(ventana,text='B) Evolución',relief=FLAT,font=('Arial',30))
    opc2.place(x=650,y=300)
    opc3=Label(ventana,text='C) Optimización',relief=FLAT,font=('Arial',30))
    opc3.place(x=650,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        buena(),
        pregunta4(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta4(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta4(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)
    
def pregunta4():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 4',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Cuál es el nivel del cual su proceso es impredecible y cuenta con muy poco control?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=200,y=100)
    label_imagen =  Label(ventana, image = imagen4)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Nivel NO establecido',relief=FLAT,font=('Arial',30))
    opc1.place(x=750,y=200)
    opc2=Label(ventana,text='B) Nivel Informal',relief=FLAT,font=('Arial',30))
    opc2.place(x=750,y=300)
    opc3=Label(ventana,text='C) Nivel Inicial',relief=FLAT,font=('Arial',30))
    opc3.place(x=750,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta5(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta5(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        buena(),
        pregunta5(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta5():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 5',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿En qué consiste el nivel 4?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen5)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Proceso Sucesor del Nivel 3',relief=FLAT,font=('Arial',30))
    opc1.place(x=470,y=200)
    opc2=Label(ventana,text='B) Procesos Avanzado Ordenado',relief=FLAT,font=('Arial',30))
    opc2.place(x=470,y=300)
    opc3=Label(ventana,text='C) En procesos medibles y predecibles',relief=FLAT,font=('Arial',30))
    opc3.place(x=470,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta6(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta6(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        buena(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta6(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)
    
def pregunta6():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 6',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que significa TSP? ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen6)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Type Process System',relief=FLAT,font=('Arial',30))
    opc1.place(x=550,y=200)
    opc2=Label(ventana,text='B) Team Process Software',relief=FLAT,font=('Arial',30))
    opc2.place(x=550,y=300)
    opc3=Label(ventana,text='C) System Process Transfusion',relief=FLAT,font=('Arial',30))
    opc3.place(x=550,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta7(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        buena(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta7(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta7(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)
    
def pregunta7():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 7',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que significa PSP?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen7)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Power System Process',relief=FLAT,font=('Arial',30))
    opc1.place(x=500,y=200)
    opc2=Label(ventana,text='B) Team Process Software',relief=FLAT,font=('Arial',30))
    opc2.place(x=500,y=300)
    opc3=Label(ventana,text='C) Personal Process Software',relief=FLAT,font=('Arial',30))
    opc3.place(x=500,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta8(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        buena(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta8(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta8(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta8():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 8',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que es MOPROSOFT? ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen8)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Montura Procesada por Software',relief=FLAT,font=('Arial',30))
    opc1.place(x=500,y=200)
    opc2=Label(ventana,text='B) Modulo de Procesamiento de Software',relief=FLAT,font=('Arial',30))
    opc2.place(x=500,y=300)
    opc3=Label(ventana,text='C) Modelo de Procesos para la Industria del Software',relief=FLAT,font=('Arial',30))
    opc3.place(x=400,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta9(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta9(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        buena(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta9(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta9():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 9',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Para qué sirve el modelo de MOPROSOFT? ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen9)
    label_imagen.place(x=1,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Administra los procesos en una empresa para un mejor resultado',relief=FLAT,font=('Arial',30))
    opc1.place(x=300,y=200)
    opc2=Label(ventana,text='B) Sirve de Guía para los tipos de procesos realizados en una Organización',relief=FLAT,font=('Arial',30))
    opc2.place(x=300,y=300)
    opc3=Label(ventana,text='C) Se encarga de mejorar y evaluar los procesos de desarrollo \ny mantenimiento de sistemas y productos de software',relief=FLAT,font=('Arial',30))
    opc3.place(x=300,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta10(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta10(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        buena(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta10(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta10():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 10',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Cuáles son las empresas que se benefician del CMMI?  ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=300,y=100)
    label_imagen =  Label(ventana, image = imagen10)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Empresas solo en México',relief=FLAT,font=('Arial',30))
    opc1.place(x=750,y=200)
    opc2=Label(ventana,text='B) Las empresas de software',relief=FLAT,font=('Arial',30))
    opc2.place(x=750,y=300)
    opc3=Label(ventana,text='C) Todas las empresas',relief=FLAT,font=('Arial',30))
    opc3.place(x=750,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta11(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=550)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        buena(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta11(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=550)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta11(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=550)

def pregunta11():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 11',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Todas las empresas se implementan igual o depende del dominio? ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=100,y=100)
    label_imagen =  Label(ventana, image = imagen11)
    label_imagen.place(x=1,y=150)

    #Etiquetas
    opc1=Label(ventana,text=
    'A) Cada empresa decide como implementar\n el modelo en su propia empresa,dependiendo\n de que es lo que necesita para mejorar'
    ,relief=FLAT,font=('Arial',30))
    opc1.place(x=450,y=200)
    opc2=Label(ventana,text='B) Team Process Software',relief=FLAT,font=('Arial',30))
    opc2.place(x=450,y=330)
    opc3=Label(ventana,text='C) System Process Transfusion',relief=FLAT,font=('Arial',30))
    opc3.place(x=450,y=430)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        buena(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta12(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta12(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta12(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)

def pregunta12():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 12',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que es SCAMPI?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen12)
    label_imagen.place(x=1,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) Evalúa una empresa desde que inicia hasta donde se estima su extinción',relief=FLAT,font=('Arial',30))
    opc1.place(x=400,y=200)
    opc2=Label(ventana,text='B) Es un método diseñado para ofrecer evaluaciones de calidad con relación a los modelos CMMI',relief=FLAT,font=('Arial',30))
    opc2.place(x=400,y=300)
    opc3=Label(ventana,text='C) Sirve de métrica para las empresas para desarrollar software',relief=FLAT,font=('Arial',30))
    opc3.place(x=400,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta13(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        buena(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta13(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta13(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)    

def pregunta13():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 13',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Para qué sirve SCAMPI?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen13)
    label_imagen.place(x=1,y=200)

    #Etiquetas
    opc1=Label(ventana,text=
    'A) Deja saber a los miembros que se les permite\n un único camino en la empresa',relief=FLAT,font=('Arial',30))
    opc1.place(x=400,y=200)
    opc2=Label(ventana,text=
    'B) Sirve de métrica para las empresas para desarrollar software',relief=FLAT,font=('Arial',30))
    opc2.place(x=400,y=300)
    opc3=Label(ventana,text=
    'C) Permite a los miembros de la empresa obtener una\n mejor comprensión sobre sus capacidades de ingeniería identificando las fortalezas y debilidades de sus procesos actuales.',relief=FLAT,font=('Arial',30))
    opc3.place(x=400,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta14(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta14(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        buena(),
        pregunta14(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)    

def pregunta14():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 14',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text='¿Que significan la sigla SCAMPI? ',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen14)
    label_imagen.place(x=1,y=400)

    #Etiquetas
    opc1=Label(ventana,text='A) Standard CMMI Appraisal Method for Process Improvement',relief=FLAT,font=('Arial',30))
    opc1.place(x=400,y=200)
    opc2=Label(ventana,text='B) CMMI Standard Evolution Improvement for Product Improvement',relief=FLAT,font=('Arial',30))
    opc2.place(x=400,y=300)
    opc3=Label(ventana,text='C) Improvement of CMMI standard evolution for the continuous improvement of processes',relief=FLAT,font=('Arial',30))
    opc3.place(x=400,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        buena(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta15(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        pregunta15(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        pregunta15(),
        opc3.destroy(),
        button11.destroy(),
        button12.destroy(),
        button13.destroy()])
    button13.place(x=1000,y=500)    



def pregunta15():
    No_pregunta = Label(ventana,text=' PREGUNTA No. 15',font=('Arial',35),bg='peach puff')
    No_pregunta.place(x=550,y=10)
    pregunta = Label(ventana,text=' ¿En dónde nació MOPROSOFT?',font=('Arial',30),bg='peach puff')
    pregunta.place(x=400,y=100)
    label_imagen =  Label(ventana, image = imagen15)
    label_imagen.place(x=100,y=150)

    #Etiquetas
    opc1=Label(ventana,text='A) En USA',relief=FLAT,font=('Arial',30))
    opc1.place(x=750,y=200)
    opc2=Label(ventana,text='B) En México',relief=FLAT,font=('Arial',30))
    opc2.place(x=750,y=300)
    opc3=Label(ventana,text='C) En Jerusalén',relief=FLAT,font=('Arial',30))
    opc3.place(x=750,y=400)

    #Botones
    button11 = Button(ventana,text='A',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        final()])
    button11.place(x=550,y=500)
    button12=Button(ventana,text='B',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        buena(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        opc3.destroy(),
        final()])
    button12.place(x=800,y=500)
    button13=Button(ventana,text='C',relief=FLAT,font=('Black Arial',40), command=lambda:[
        No_pregunta.destroy(),
        pregunta.destroy(),
        label_imagen.destroy(),
        opc1.destroy(),
        opc2.destroy(),
        final()])
    button13.place(x=1000,y=500)  

def final():
    ventana.destroy()
    ventana2 = Tk()
    ventana2.title(">>> ☼ RESULTADO ☼ <<<")
    ventana2.state("zoomed")

    #global names, puntos

    totalDePuntos = (puntos*100)/15

    if totalDePuntos<60:
        ventana2.config(bg = "red")
        info=Label(ventana2,text=
        (f"Hola {names} su Puntuaje es --> {totalDePuntos:.3}/100"),relief=FLAT,font=('Arial',30))
        info.place(x=200,y=200)
    else:
        ventana2.config(bg = "green")

    ventana2.mainloop()

#-----------------------------------------------------------------------------------------------------------
# Interfaz Grafica
ventana = Tk()
ventana.title('>> Quiz App <<<')
#ventana.geometry("500x600") #Definir Tamaño de la Ventana Manualmente
#ventana.attributes("-fullscreen", True) #Pantalla Completa como en Juegos
ventana.state('zoomed') #Abrir Ventana Maximizada
ventana.config(bg = "peach puff")
ventana.iconbitmap("iconoDeVentanita.ico") #Poner Icono a la Ventana

#Menú de Inicio
label_Title = Label(ventana, text='Quiz',font=('Arial',50),bg='peach puff')
label_Title.place(x=600,y=50)
campo_Nombre=Label(ventana, text='USERNAME',font=('Arial',30),bg='peach puff')
campo_Nombre.place(x=300,y=250)
entry1=Entry(ventana,font=('Arial',30))
entry1.place(x=600,y=250)

name=entry1.get()

names = name

botonJugar = Button(ventana, text='Play',font=('Arial',30), command = pregunta1)
botonJugar.place(x = 550, y = 450)

#Declarar Imagenes
imagen = PhotoImage(file ='1.png')
imagen2 = PhotoImage(file ='2.png')
imagen3o = PhotoImage(file ='3.png')
imagen3= imagen3o.zoom(2)
imagen4o = PhotoImage(file ='4.png')
imagen4 = imagen4o.zoom(2)
imagen5 = PhotoImage(file ='5.png')
imagen6o = PhotoImage(file ='6.png')
imagen6 = imagen6o.subsample(3)
imagen7o = PhotoImage(file ='7.png')
imagen7 = imagen7o.subsample(2)
imagen8 = PhotoImage(file ='8.png')
imagen9o = PhotoImage(file ='9.png')
imagen9 = imagen9o.subsample(2)
imagen10o = PhotoImage(file ='10.png')
imagen10 = imagen10o.subsample(3)
imagen11o = PhotoImage(file ='11.png')
imagen11 = imagen11o.subsample(2)
imagen12o = PhotoImage(file ='12.png')
imagen12 = imagen12o.subsample(2)
imagen13o = PhotoImage(file ='13.png')
imagen13 = imagen13o.subsample(3)
imagen14 = PhotoImage(file ='14.png')
imagen15 = PhotoImage(file ='15.png')

ventana.mainloop()
