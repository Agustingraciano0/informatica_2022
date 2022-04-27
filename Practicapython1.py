#Ej 1
def largo(string):
    return len(string)

#Ej 2 
def cinco_seis (string):
  if len (string) >= 5:
    return str.upper (string [4:5])
  else:
    return "error"

#Ej 3 
def saludar (nombre, apellido):
  return "Holis " + nombre + " " + apellido

print (saludar("agustin", "graciano"))

#Ej 4 
def nombre_completo (nombre, apellido):
  return str.title (nombre), str.title (apellido)

print (nombre_completo("agustin","graciano"))

#Ej 5
def promedio (n1,n2,n3):
  return(n1+n2+n3)/3

print (promedio(5,4,7))

#Ej 6 
def horario(minutos):
  return str(int(minutos/60))+ "horas y " + str(minutos%60)+ "minutos" 

  print(horario(200))
#va % porque se necesita tener un resto y el % es el resto en la computadora

#Ej 7 
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

