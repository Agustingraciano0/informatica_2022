#Ej 1
#Escribir un programa que imprima la longitud de un string el cual se lee por teclado.
def largo(string):
    return len(string)

#Ej 2 
#Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).
def cinco_seis (string):
  if len (string) >= 5:
    return str.upper (string [4:5])
  else:
    return "error"

#Ej 3 
#Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.
def saludar (nombre, apellido):
  return "Holis " + nombre + " " + apellido

print (saludar("agustin", "graciano"))

#Ej 4 
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas
def nombre_completo (nombre, apellido):
  return str.title (nombre), str.title (apellido)

print (nombre_completo("agustin","graciano"))

#Ej 5
#Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.
def promedio (n1,n2,n3):
  return(n1+n2+n3)/3

print (promedio(5,4,7))

#Ej 6 
#Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.
def horario(minutos):
  return str(int(minutos/60))+ "horas y " + str(minutos%60)+ "minutos" 

  print(horario(200))
#va % porque se necesita tener un resto y el % es el resto en la computadora

#Ej 7 
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza
# Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.
def sueldo (sueldo_base, ventas):
  if ventas >= 4:
    return sueldo_base + (sueldo_base * 0.1)* ventas
  else:
    return sueldo_base

print(sueldo(4000,8))

#Ej 8 
def nota_final(correctas,incorrectas,blanco):
   return correctas*4 + incorrectas * (-1) + blanco *0
nota_final(3,2,2)

