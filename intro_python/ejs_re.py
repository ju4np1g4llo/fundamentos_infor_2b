# **Expresiones Regulares**

##### **Ejercicio 1**

from ast import Not
import re

def verificar(string):
    if re.search(r"[a-zA-Z0-9]", string):
        print("Tiene al menos uno de los caracteres")
    else:
        print("No tiene al menos uno de los caracteres")

##### **Ejercicio 2**

import re

def verificar(string):
    if re.search(r"\W", string):
        print("Tiene algun caracter no permitido")
    else:
        print("Tiene todos los caracteres permitidos")

##### **Ejercicio 3**
#Creá un programa que verifique las siguientes condiciones:
    
#* si un string dado tiene una _h_ seguida de ninguna o más _e_.
import re 

def encontrar_patron(string):
    patron ="he*"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
        
#* si un string dado tiene una _h_ seguida de una o más _e_.
import re

def encontrar_patron(string):
    patron ="he+"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"
#* si un string dado tiene una _h_ seguida de una o más _e_.
#esta repetido
#* si un string dado tiene una _h_ seguida de dos o tres _e_.
import re

def encontrar_patron(string):
    patron ="he{2,3}"
    if re.search(patron, string) is not None:
        return "Se encontro el patron"
    else:
        return "No se encontro el patron"

##### **Ejercicio 4*
import re

def unida(string):
    return re.findall(r"(\w+)_(\w+)", string)

##### **Ejercicio 5**
#Escribí un programa que diga si un string empieza con un número específico.

def empieza(string,numero):
    print(bool(re.search("^"+str(numero),string)))

##### **Ejercicio 6**
#Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada.

def verLista(string):
    aparecen = []
    lista = ["Habia","una","vez","algo"]
    for i in lista:
        if re.search(i,string) is not None:
            aparecen.append(i)
        else:
            None
    print(aparecen)

##### **Ejercicio 7**
#Realizá un programa que encuentre un string que contenga solamente letras minúsculas, mayúsculas, espacios y números.

def minMayEspN(string):
    if re.search(r"([^\w\s]+)",string):
       print("Tiene algun caracter no valido")
    else:
        print("El string esta bien")            #creo que no pide esto

##### **Ejercicio 8**
#Escribí un programa que separe y devuelva los caracteres númericos de un string.

def numeros_en_string(string):
    print(re.findall("[0-9]",string))

##### **Ejercicio 9**
#Escribí un programa que extraiga los caracteres que estén entre guiones en un string. (String de ejemplo: _"Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"_)

import re

def entre_guiones(string):
    return re.findall(r"-(.*?)-", string)

string = "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-"

print(entre_guiones(string))

##### **Ejercicio 10**
#Obtené las substrings y las posiciones de estas en una string dada considerando que las substrings están delimitadas por los caracteres _@_ o _&_.

def substrings(string):
    return re.findall(r"[@&](.*?)[@&]",string)

# r"-([\w+_-]@[\w+]\.[a-z]{2-6})-"     patron que puede buscar mails visto en clase practica    
       
##### **Ejercicio 11**
#Realizá un programa que dado una lista de strings verifique que dos palabras dentro del string empiecen con la letra P y las imprima. (Lista de ejemplo: _["Práctica Python", "Práctica C++", "Práctica Fortran"]_).
import re

def dos_p(lista):
    for elemento in lista:
        resultado = re.match("(P\w*)\W(P\w*)", elemento)
        if resultado is None:
            print(resultado.group())


##### **Ejercicio 12**
#Escribí un programa que reemplace todas las ocurrencias de espacios, guiones bajos y dos puntos por la barra vertical (**|**).

def reemplazar(string):
        return re.sub(r"[:_\s]","|",string)

##### **Ejercicio 13**
#Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos.

def dos_no_alfa(string):
    print(re.sub(r"\W","_",string,2))   #la llave dice que hayan 2 que esten juntos, el 2 a la derecha del string indica que sean los primeros 2 que aparecen en todo el string.


##### **Ejercicio 14**
#Realizá un programa que reemplace los espacios y tabulaciones por punto y coma.

def reemplazar2(string):
        return re.sub(r"[\t\s]",";",string)

##### **Ejercicio 15**
#Realizá un programa que validar si una cuenta de mail está escrita correctamente.

def mail(mail):
    print(bool(re.match(r"(\S+)@(\w+)\.(\w+)",mail)))                                                           