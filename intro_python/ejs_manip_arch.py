# **Manipulación de archivos**

##### **Ejercicio 1**
#Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo **no** empiezan con una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P").
from re import I


def noP(archivo):
    with open(archivo,"r") as f:
        hayP = f.read().split()
        sinP=[]
        for i in hayP:
            if i[0] == "P":
                None
            elif i[0] == "p":         #podia haber hecho si era != a P/p que sume a la lista en vez de 2 None
                None
            else:
                sinP.append(i)
        print(len(sinP)) 
        #print(sinP)

##### **Ejercicio 2**
#Escribí un programa que lea un archivo e imprima las primeras n líneas.

def primeras_lineas(archivo,numero):
    with open(archivo,"r") as f:
        a = f.readlines()
        return a[0:numero]

##### **Ejercicio 3**
#Escribí un programa que lea un archivo, guarde las líneas del archivo en una lista y luego imprima las n últimas.

def ultimas_lineas(archivo,numero):
    with open(archivo,"r") as f:
        a = f.readlines()
        lenA = len(a)
        lineasInic = lenA - numero
        print(a[lineasInic:lenA])

##### **Ejercicio 4**
#Hacé un programa que lea un archivo, cuente la cantidad de palabras del archivo y luego imprima el resultado.

def contar(archivo):
    with open(archivo,"r") as f:
        print(len(f.read().split()))

##### **Ejercicio 5**
#Escribí un programa que lea un archivo, reemplace una letra por esa misma letra más un salto de línea y lo guarde en otro archivo.

#def reemplazar(archivo,letra):
    #with open(archivo,"r") as f:
        #palabras = f.read().split()         #solo se me ocurre con re, x lo que no estaria bien ya que esto era antes de ver re
'''no terminado'''                     

##### **Ejercicio 6**

def borrar_salto(arch1, arch2):
    with open(arch1, "r") as f, open(arch2, "w") as f2:
        for line in f:                     #faltaba el for
            f2.write(line.strip("\n"))       #.strip saca todo lo que este entre las comillas

##### **Ejercicio 7**

def palabra_larga(archivo):
    palabra = ""
    max_long = 0
    with open(archivo, "r") as f:
        lista_palabras = f.read().split()
        for word in lista_palabras:
            if len(word) > max_long:
                max_long = len(word)
                palabra = word
        print(palabra)
        print(max_long)

##### **Ejercicio 8**

def unir(arch1, arch2, arch3):
    with open(arch1, "r") as ar1, open(arch2, "r") as ar2, open(arch3, "a") as ar3:
        ar3.write(ar1.read() + ar2.read())
#en este no se hacen 3 with open, con un solo with ya sirve

##### **Ejercicio 9**


dict1= {}
def cuenta(archivo):
    frecuencias = dict1()
    with open(archivo, "r") as f:
        palabras_lista = f.read().split()      #el .split separa las palabras en un archivo
        for i in palabras_lista:
            if i in frecuencias:
                frecuencias[1] += 1
            else:
                frecuencias[1] = 1
        for palabra in frecuencias.keys():
            frecuencias[palabra] = round(frecuencias[palabra] / len(palabras_lista), 3)
    print(frecuencias)

##### **Ejercicio 10**

import os
import glob

def funcion1(archivo, ruta):
    os.chdir(ruta)
    lista_txt = glob.glob("*.txt")
    with open(archivo, "a") as s:
        for file in lista_txt:             #por cada archivo en lista_txt
            s.write(file.read())           #agarra y escribe en el archivo "s" lo de otro archivo
            file.close()