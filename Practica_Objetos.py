#Ejercicio 1
from msilib.schema import Class, SelfReg
from re import L
from tkinter import _ExceptionReportingCallback

class Perro:
    def _init_ (self):
        self._alimento = 0
        self._caricias = 0
    
    def energia (self):
        return self._alimento + (self._caricias*10)
    
    def comer (self, gramos):
        self._alimento += gramos
    
    def acariciar (self):
        self._caricias += 1
    
    def estaDebil (self):
        return self._caricias < 2

perro = Perro()
print(perro.comer(100))
print(perro._alimento)
print(perro.acariciar())
print(perro._caricias)
print(perro.energia())

#Ejercicio 2



#Ejercicio 3 
class Notebook:
    def _init_ (self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def descuento (self, porcentaje):
        descuento1= self.precio *(porcentaje/100)
        print("el valor es de " + str(descuento1 + self.precio))


compu1 = Notebook("Mac", "thinkpad", 100)
compu1.descuento (10)

#Ejercicio 4
class Contador:
    def _init_ (self,valor):
        self.valor = valor
    def inc (self):
        self.valor += 1
    def dis(self):
        self.valor -=1
    def reset (self):
        self.valor = 0
    def valorActual (self):
        print(self.valor)
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
    
contador =  Contador (10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(15)
contador.dis()
contador.dis()
contador.valorActual()

#Ejercicio 6




