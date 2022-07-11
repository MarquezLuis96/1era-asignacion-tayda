# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 14:48:46 2022

@author: ORDENADOR
"""
# LIBRERIAS DE INTERFAZ
from tkinter import Tk
from tkinter import ttk
from tkinter import Entry
from tkinter import Label
from tkinter import StringVar

#lIBRERIA PARA BUSCAR ARCHIVO EN EL DISCO
from tkinter import filedialog

#LIBRERIA HEAPSORT
from heapq import heappop, heappush

#LIBRERIA PARA GRAFICAR
import matplotlib.pyplot as plt

#LIBRERIA CRONOMETO
import time

# SELECCIONA EL DOCUMENTO
def abrir():
    
    ventana.filename = filedialog.askopenfilename(initialdir = "C:/Users",title = "Elige archivo:", filetypes = (("Ficheros de texto","*.txt"),("Todos los ficheros","*.*")))
    # VARIBLE DONDE SE ALMACENA LA DIRECCION DEL DOCUMENTO
    global ruta
    ruta = ventana.filename
    direccion.set(ruta)
    
    ventana.mainloop()


# GRAFICA UNA FUNCION
def graficar(A,t):
    
    x = [0,len(A)]
    y = [0,t]
    
    plt.plot(x,y)
    
    plt.title("TIEMPO DE ORDENAMIENTO")
    plt.xlabel("ENTRADA")
    plt.ylabel("TIEMPO")
    
    plt.show()


# GRAFICA DOS FUNCIONES   
def graficar2(A,t1,t2):
    
    x = [0,len(A)]
    y = [0,t1]
    
    plt.plot(x,y,label='f1')
    
    x = [0,len(A)]
    y = [0,t2]
    
    plt.plot(x,y,label='f2')
    
    plt.title("TIEMPO DE ORDENAMIENTO")
    plt.xlabel("ENTRADA")
    plt.ylabel("TIEMPO")
    
    plt.show()

# Metodo de selección
def seleccion(A,n):
    
    # Tiempo de inicio
    inicio = time.time()
    
    for i in range(len(A)):
        
        minimo=i
        
        # Compara desde la posición i hasta el final del arreglo
        for j in range(i,len(A)):
            
            # Busca el indice del valor mínimo
            if(int(A[j]) < int(A[minimo])):
                
                minimo = j
        
        # Si minimo no está en posición i (0) se intercambia.
        if(minimo != i):
            
            aux = A[i]
            
            A[i] = A[minimo]
            
            A[minimo] = aux
            
    # Tiempo final
    fin = time.time()
    
    # Tiempo total
    tiempo = fin-inicio
    
    if n==1:
        graficar(A,tiempo)
    else:
        return tiempo
    
    return A


def heapsort(A,n):
    
    # Tiempo de inicio
    inicio = time.time()
    
    # Lista que será el montón
    heap = []
    
    for element in A:
        
        """ 
        heappush(list, item): Agrega un elemento al montón y lo 
        reordena posteriormente para que siga siendo un montón. 
        Se puede usar en una lista vacía.
        """
        heappush(heap, int(element))
    
    
    # Lista donde de insertarán los elementos ordenados
    ordenado = []

    # Mientras halla elementos en el montón
    while heap:
        """"
        heappop(list): Pops (elimina) el primer elemento 
        (más pequeño) y devuelve ese elemento.
        """
        ordenado.append(heappop(heap))
    
    # Tiempo final
    fin = time.time()
    
    # Tiempo total
    tiempo = fin-inicio
    
    if n==1:
        graficar(ordenado,tiempo)
    
    if n==2:
        escribir(ordenado)
        return tiempo
    
    return ordenado


# GUARDA EL ARCHIVO DE TEXTO ORDENADO
def escribir(A):
    
    # SE ABRE EL ARCHIVO EN MODO WRITE
    file = open("ordenado.txt", "w")
    
    # SOLO PUEDE ESCRIBIR CADENA DE CARACTERES
    # str() TRANSFORMA ENTERO A STRING
    
    for i in range(0,len(A)):
        
        file.write(str(A[i])+"\n")
    
    # SE CIERRA EL ARCHIVO AL FINALIZAR
    file.close()

# ALMACENA LOS DATOS EN UNA LISTA
def leer(n):
    
    A = []
    
    global ruta
    
    # SE ABRE EL ARCHIVO EN MODO READ
    file = open(ruta,"r")
    
    # LEE LA PRIMERA LINEA
    linea = file.readline()
    
    dig = linea[0:-1]
    A.append(dig)
    
    # LINEA NO ESTÉ VACIA
    while linea!='':
        
        # LEE LA PRÓXIMA LINEA
        linea = file.readline()
        # NO SE COPIAN LOS ULTIMOS DOS CARACTERES '\n'
        dig = linea[0:-1]
        # SI LA LINEA ESTÁ VACIA
        if dig != '':
            A.append(dig)
        
    # CIERRA EL ARCHIVO AL FINALIZAR
    file.close()
    
    if n==1:
        O = seleccion(A,1)
        # SE GUARDA EL DOCUMENTO ORDENADO
        escribir(O)
    if n==2:
        O = heapsort(A,1)
        # SE GUARDA EL DOCUMENTO ORDENADO
        escribir(O)
    if n==3:
        tiempo1 = seleccion(A,2)
        tiempo2 = heapsort(A,2)
        graficar2(A,tiempo1,tiempo2)


def interfaz():
    
    global ventana
    global direccion
    
    ventana = Tk()
    ventana.geometry('370x200')
    ventana.title("MÉTODOS DE ORDENAMIENTO")
    
    
    bElegir = ttk.Button(ventana, text="Elegir", command=abrir).place(x=10,y=30)
    
    direccion = StringVar()
    Label(text = "DIRECCIÓN DEL DOCUMENTO", font= ("Times New Roman",10)).place(x=100, y=10)
    entry = Entry(ventana, textvariable = direccion, state="readonly", width = 40).place(x=100, y=32)
    
    Label(text = "MÉTODO DE ORDENAMIENTO", font= ("Times New Roman",10)).place(x=100, y=75)
    bSeleccion = ttk.Button(ventana, text="Método de selección", command= lambda: leer(1)).place(x=50,y=95)
    bHeapsort = ttk.Button(ventana, text="Método heap sort", command= lambda: leer(2)).place(x=200,y=95)
    bAmbos = ttk.Button(ventana, text="Ambos métodos", command= lambda: leer(3)).place(x=130,y=135)
    
    ventana.mainloop()
    

interfaz()