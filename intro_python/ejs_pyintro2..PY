# **Práctica de introducción a Python - Parte 2**

##### **Ejercicio 1**

def may_o_min(palabra):
  for l in palabra:
    if l[0].islower():
      return "Es minuscula"
    else:
      return "Es mayuscula"

##### **Ejercicio 2**

def numero():
  numero = int(input("Dame un numero: "))
  if numero > 0:
    return "Es positivo"
  elif numero < 0:
    return "Es negativo"
  else:
    return "Es igual a cero"

##### **Ejercicio 3**

def dado():                                     
  numero = int(input("Dame un numero entre el 1 y el 6 (incluidos estos 2): "))
  if numero == 1:
    return "El opuesto en el dado es el OPUESTO DEL 1"
  elif numero == 2:
    return "OPUESTO DEL 2"
  elif numero == 3:
    return "OPUESTO 3"
  elif numero == 4:
    return "OPUESTO 4"
  elif numero == 5:
    return "OPUESTO 5"
  elif numero == 6:
    return "OPUESTO 6"
  else:
    return "El numero es incorrecto"

##### **Ejercicio 4**

def paquete():
    AméricadelSur = 10 
    AméricaCentral = 15
    AméricadelNorte = 18
    Europa = 24
    Asia = 30
    peso_paquete = int(input("Escriba el peso de su paquete en gramos: "))
    continente = input("Elija su continente (América del Sur/América Central/América del Norte/Europa/Asia): ")
    if peso_paquete > 5000:
        return "Su paquete no puede ser llevado"
    elif continente == "América del Sur":
        return "Su paquete cuesta $" + str(peso_paquete * AméricadelSur)
    elif continente == "América Central":
        return "Su paquete cuesta $" + str(peso_paquete * AméricaCentral)
    elif continente == "América del Norte":
        return "Su paquete cuesta $" + str(peso_paquete * AméricadelNorte)
    elif continente == "Europa":
        return "Su paquete cuesta $" + str(peso_paquete * Europa)
    else:
        return "Su paquete cuesta $" + str(peso_paquete * Asia)
       

##### **Ejercicio 5**

def dia():
  dia_semana = int(input("Numero de dia de la semana: "))
  if dia_semana == 1:
    return "Hoy es Lunes"
  elif dia_semana == 2:
    return "Hoy es Martes"
  elif dia_semana == 3:
    return "Hoy es Miercoles"
  elif dia_semana == 4:
    return "Hoy es Jueves"
  elif dia_semana == 5:
    return "Hoy es Viernes"
  elif dia_semana == 6:
    return "Hoy es Sabado"
  elif dia_semana == 7:
    return "Hoy es Domingo"
  else:
    return "Numero no válido"

### Listas

##### **Ejercicio 6**
#Creá una lista e inicializala con 5 cadenas de caracteres leídas por teclado. Copiá los elementos de la lista en otra lista pero en orden inverso, imprimí los elementos de esta última lista.
#Recordá que la manera de copiar una lista en otra es:_

#python
#lista2 = list(lista1)


##### **Ejercicio 7**

lista = []
def llenar():
  numero = int(input("Dame un numero: "))
  if numero >= 0:
    lista.append(numero)
    print(lista)
    llenar()
  else:
    print(lista)

##### **Ejercicio 8**
#Realizá un programa que declare tres listas _lista1_, _lista2_ y _lista3_, donde las dos primeras listas deben tener cinco enteros cada una, ingresados por teclado y asigne para cada elemento de la _lista3_ la suma de los elementos de la _lista1_ y la _lista2_ (es decir, el primer elemento de la _lista3_ tiene que ser la suma del primer elemento de la _lista1_ y el primero de la _lista2_)

def listas():
  lista1 = []
  lista2 = []


##### **Ejercicio 9**

edades = []
nombres = []
lista_index = []
def tl():
  nombre = input("Nombre del alumno: ")
  if nombre != "*":
    nombres.append(nombre)
    edad = int(input("Edad del alumno: "))
    edades.append(edad)
    tl()
  else:
    max_edades = max(edades)
    print(max_edades)
    count = 0
    if edades.count(max_edades) > 1:
        for i in edades:
            if max_edades == i:
                lista_index.append(count)
            count += 1 
    for i in lista_index:
        print(nombres[i]) 
    


### Diccionarios

##### **Ejercicio 10**

def contador():
  contadores = {}
  cadena = input("Escribi una cadena: ")
  for caracter in cadena:
    if caracter in contadores:
      contadores[caracter]+=1
    else:
      contadores[caracter]=1
  for clave,valor in contadores.items():
    print(clave,valor)

##### **Ejercicio 11**

def contador_mod():
  alfabeto = "abcdefghijklmnñopqrstuvwxyz"
  contadores = {}
  for letra in alfabeto + alfabeto.upper():
    contadores[letra]=0
  cadena = input("Escribi una cadena: ")
  for caracter in cadena:
    if caracter.lower() in alfabeto:
      contadores[caracter]+=1
  for clave,valor in contadores.items():
    print(clave,valor)

##### **Ejercicio 12**
#Creá un programa que permita guardar los nombres de los alumnos de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guardá la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de cada alumno.
#El programa tiene que pedir el número de alumnos que se va a introducir, luego su nombre y sus notas hasta que introduzcamos un número negativo. Al final el programa tiene que mostrar la lista de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya existe el programa tiene que dar un error.

### Funciones

##### **Ejercicio 13**

def esMultiplo():
    n1 = int(input("Dame un número: "))
    n2 = int(input("Dame otro número: "))
    if (n1 > n2) and (n1 % n2 == 0):
        return "Son Multiplos"
    elif (n1 > n2) and (n1 % n2 != 0):
        return "No son multiplos"
    elif (n2 > n1) and (n2 % n1 == 0):
        return "Son Multiplos"
    else:
        return "No son multiplos"

##### **Ejercicio 14**
#Creá una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. 
# Escribí un programa principal, que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa tiene que pedir el número de días que se van a introducir.


def promedio():
  maxima = int(input("Escriba la maxima del dia: "))
  minima = int(input("Escriba la minima del dia: "))
  suma = maxima + minima
  promedio = suma / 2
  return promedio


def temperatura():
  dias = int(input("Cantidad de dias a calcular: "))
  promedio()                      #no se me ocurre nada para hacer la segunda parte




##### **Ejercicio 15**

def cargarSocios(socios):                               #hecho por guille en la clase que fue virtual
    numero = int(input("Número de socio: "))
    while numero != 0:
        nombre = input("Nombre y apellido: ")
        fecha = input("Fecha de ingreso: ")
        cuota = input("¿Cuota al día? s/n: ")
        pago = cuota.lower() == "s"
        socios[numero] = [nombre, fecha, pago]
        numero = int(input("Número de socio: "))
    return socios

def modificarFecha(socios, fechaAnterior, fechaNueva):
    for datos in socios.values():
        if datos[1] == fechaAnterior:
            datos[1] = fechaNueva
    return socios

def numeroSocio(socios, nombre):
    for numero,datos in socios.items():
        if datos[0].lower() == nombre.lower():
            return numero
    return 0

def formatoFecha(fecha):
    return fecha[:2] + "/" + fecha[2:4] + "/" + fecha[4:]

def imprimirListado(socios):
    for numero,datos in socios.items():
        print("Número: ", numero)
        print("Nombre: ", datos[0])
        print("Fecha de ingreso ", formatoFecha(datos[1]))

    if datos[2]:
            print("Cuota al día")
    else:
            print("En deuda")
    print("---------------")
    return None

socios_activos = {1: ["Florencia Ocampo", "14092001", True], 2: ["David Estévez", "14092001", True], 3: ["Sofía Cáceres", "14092001", True]}

print("Cargar socios")
socios_activos = cargarSocios(socios_activos)

print("El club tiene", len(socios_activos), "socios")

print("Registrar pago de cuotas")
numero = int(input("Numero de socio: "))
socios_activos[numero][2] = True

print("Modificando fecha de ingreso...")
socios_activos = modificarFecha(socios_activos, "21102017", "22102017")

print("Eliminar socio:")
nombre = input("Nombre y apellido: ")
numero = numeroSocio(socios_activos, nombre)
del socios_activos[numero]

imprimirListado(socios_activos)
