from cgitb import text
import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
from ClaseAPI import CONSULTAAPI

class Aplicacion(tk.Tk):
    __dolar=None
    __pesos=None
    def __init__(self):
        self.__consulta=CONSULTAAPI()
        self.__consulta.run()
        super().__init__()
        self.title('Conversor de USD a ARS')
        self.config(padx=10,pady=10)

        self.__dolar=StringVar()
        self.__pesos=StringVar()
        self.__dolar.trace('w',self.Calcular)

        ttk.Label(self,text="dolares").grid(column=2,row=0)
        self.entryDolar=ttk.Entry(self,width=10,textvariable=self.__dolar)
        self.entryDolar.grid(column=1,row=0)

        ttk.Label(self,text="pesos").grid(column=2,row=1)
        ttk.Label(self,text="equivale a: ").grid(column=0,row=1)
        ttk.Label(self,textvariable=self.__pesos).grid(column=1,row=1)

        ttk.Button(self, text="Salir", command=self.destroy).grid(column=2, row=5, sticky='E', padx=2)
    
    def Calcular(self,*args):
        if self.entryDolar.get() != '':
            try:
                val=float(self.entryDolar.get())
                self.__pesos.set(val*self.__consulta.getPrecio())
            except ValueError:
                messagebox.showerror(er="ERROR DE TIPO",message="SOLO INGRESAR VALORES NUMERICOS")
                self.__dolar.set('')
                self.entryDolar.focus()
        else:
            self.__pesos.set('')