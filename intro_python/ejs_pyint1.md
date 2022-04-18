# **Práctica de introducción a Python - Parte 1**
_Antes de iniciar con los ejercicios asegúrense de tener instalado correctamente Python y un IDE (preferentemente Visual Studio Code). Además, en los sistemas que tengan Linux y Mac tienen que tener instalado Bash._

##### **Ejercicio 1**
 Escribir un programa que imprima la longitud de un string el cual se lee por teclado.

 def longitud(string):
    print(len(string)) 

##### **Ejercicio 2**
Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).

def letras(string):
    print(string[4:6])

##### **Ejercicio 3**
Escribir un programa que pregunte el nombre y apellido al usuario y lo salude.

def saludo():
    nombre_y_apellido = input("Escriba su nombre y apellido: ")
    print("Hola " + nombre_y_apellido + ", ¿que tal?")

##### **Ejercicio 4**
Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales en mayúsculas

def mayusculas():
    nombre = input("Escriba su nombre: ")
    apellido1 = input("Escriba su primer apellido: ")
    apellido2 = input("Escriba su segundo apellido: ")
    print(str.upper(nombre[0])) 
    print(str.upper(apellido1[0])) 
    print(str.upper(apellido2[0]))

##### **Ejercicio 5**
Realizar un programa que lea tres números por teclado y calcule el promedio de ellos.

def numeros(numero1, numero2, numero3):
    suma = numero1 + numero2 + numero3
    promedio = suma/3
    print(promedio)

##### **Ejercicio 6**
Dada una cierta cantidad de minutos (ingresada por teclado) hacer un programa que muestre cuántas horas y minutos son. Por ejemplo 150 minutos son 2 horas y 30 minutos.

def horas():
    minutos = int(input("Diga la cantidad de minutos: "))
    horas = minutos/60
    print(horas)

           #no le encuentro la vuelta

##### **Ejercicio 7**
Un comerciante, el cual tiene un sueldo base, recibe un 10% extra por comisión por cada venta que realiza. Realizar un programa que devuelva el dinero que recibirá por comisión luego de 4 ventas y el total de dinero que ganará ese mes, teniendo en cuenta estas ventas y su sueldo base.

##### **Ejercicio 8**
Escribir un programa para calcular la nota final de un estudiante, teniendo en cuenta que por cada respuesta correcta el estudiante suma 4 puntos, por cada incorrecta se le resta 1 punto y si la respuesta está en blanco no se le suma ni se le resta.

u
