#Ejercicio 1
"""
Estado: El estado de un objeto es el cojunto de atributos del objeto. En este caso, el estado es self o alimento y caricias.
Interfaz: La interfaz de un objeto es el conjunto de mensajes que cada objeto expone. En este caso seria energia, comer, acariciar, esta debil.
"""
#Ejercicio 2
#
# Modificá el método volar de la clase 
#Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.
from wsgiref.validate import validator


def volar(self, kms):
    if self.energia >0:
        self.energia -= 10 + kms/10
    else:
        print("No puede volar")


#Ejercicio 3
#Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio
#el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver 
#cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.
class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio

    def descuento_precio(self, porcentaje):
        self.precio = self.precio - (self.precio * porcentaje / 100)


#Ejercicio 4
#Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. 
# También puede resetear este valor y al hacerlo se pone en cero
#Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:
#inc()
#dis()
#reset()
#valorActual()
#valorNuevo(nuevoValor)

class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
    
    def inc(self):
        self.valor_inicial += 1
    
    def dis(self):
        self.valor_inicial -= 1
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo

    def valorActual(self):
        return self.valor_inicial


#Ejercicio 5
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. 
#Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo).
#El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
    def __init__(self, valor_inicial):
        self.valor_inicial = valor_inicial
        self.lista1 = []
    def inc(self):
        self.valor_inicial += 1
        self.lista1.append("incremento")
    
    def dis(self):
        self.valor_inicial -= 1
        self.lista1.append("disminucion")
    
    def reset(self):
        self.valor_inicial = 0
    
    def valorNuevo(self, valor_nuevo):
        self.valor_inicial = valor_nuevo
        self.lista1.append("actualizacion")

    def valorActual(self):
        return self.valor_inicial
    
    def ultimoComadando(self):
        return self.lista1[-1]


#Ejercicio 6
#Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. 
# Este objeto debe entender los siguientes mensajes:
#cargar(numero)
#sumar(numero)
#restar(numero)
#multiplicar(numero)
#valorActual()

class Calculadora:
    def __init__(self):
        self.valor = 0
    
    def cargar(self, numero):
        self.valor = numero

    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor = self.valor*numero

    def valorActual(self):
        return self.valor


#Ejercicio 7
#Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS 
# (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”)
#El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere
#El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió.
#El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None
#Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.


class Gorriones:
    def __init__(self):
        self.gramos = 0
        self.kilometros = 0
        self.gramoscomidos = []
        self.kilometrosvolados = []

    def comer(self, gramos):
        self.gramos += gramos
        self.gramoscomidos.append(gramos)

    def volar(self, kilometros):
        self.kilometros += kilometros
        self.kilometrosvolados.append(kilometros)
    
    def CSS(self):
        if self.gramos > 0:
            return self.kilometros/self.gramos
        else:
            return "None"

    def CSSP(self):
        if self.gramos > 0: 
            return max(self.kilometrosvolados)/max(self.gramoscomidos) 
        else:
            return "None"
    def CSSV(self):
        if self.gramos > 0: 
            return len(self.kilometrosvolados)/len(self.gramoscomidos)
        else:
            return "None"  

    def esta_en_equilibrio(self):
        return 0.5 < self.CSS() < 2
