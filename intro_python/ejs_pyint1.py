

##### **Ejercicio 1**
 

def longitud(string):
    print(len(string)) 

##### **Ejercicio 2**


def letras(string):
    print(string[4:6])

##### **Ejercicio 3**


def saludo():
    nombre_y_apellido = input("Escriba su nombre y apellido: ")
    print("Hola " + nombre_y_apellido + ", ¿que tal?")

##### **Ejercicio 4**


def mayusculas():
    nombre = input("Escriba su nombre: ")
    apellido1 = input("Escriba su primer apellido: ")
    apellido2 = input("Escriba su segundo apellido: ")
    print(str.upper(nombre[0])) 
    print(str.upper(apellido1[0])) 
    print(str.upper(apellido2[0]))

##### **Ejercicio 5**


def numeros(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    promedio = suma/3
    print(promedio)

##### **Ejercicio 6**


def horas():
    minutos = int(input("Diga la cantidad de minutos: "))
    horas = (minutos/60)
    print(horas)

           #no le encuentro la vuelta

##### **Ejercicio 7**
#Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. 
#Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, 
#teniendo en cuenta estas ventas y su sueldo base.

##### **Ejercicio 8**
#Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, 
#por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.



