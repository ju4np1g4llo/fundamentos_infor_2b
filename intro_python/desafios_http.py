from calendar import c
from this import d
from turtle import home
import requests

r = requests.get('https://macowins-server.herokuapp.com/prendas')
#print(r.json())
#print(r.status_code)


#Desafio III 
#contrastá con lo que sucede al hacer get de 'https://macowins-server.herokuapp.com/prendas/1' ¿Qué te devuelve el método headers? ¿Qué status_code obtenes?
r = requests.get("https://macowins-server.herokuapp.com/prendas/1")
r.headers
r  #"<Response [200]>"

#Desafio IV
#¿y que sucederá si consultamos a una dirección que no existe, como por ejemplo https://macowins-server.herokuapp.com/prindas/1? ¡Averigualo!

print(requests.get("https://macowins-server.herokuapp.com/prindas/1"))
#"<Response [404]>"

#Desafio V
#hacé requests.get('https://macowins-server.herokuapp.com/ventas') y requests.get('https://macowins-server.herokuapp.com/ventas/2)' y contrastá el resultado con tu respuesta anterior

print(requests.get('https://macowins-server.herokuapp.com/ventas'))
print(requests.get('https://macowins-server.herokuapp.com/ventas/2'))
#La barra / no afecta si no tiene un numero al lado, por lo qe buscara como si no tuviese
#Los 2 te devuelven Response 200 porque puede encontrar algo

#Desafio VI
#Obtené las remeras.

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
print(r.json())

#Desafio VII
#Obtené las remeras XS

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
print(r.json())

#Desafio VIII
#decí usando tus palabras qué significa la URI de este ejemplo cerebral 
#Está definiendo que la URL busque el recuerdo de la clase de http de hoy en nuestro cerebro como una "pagina web"

#Desafio IX
#¿a través de qué IP accedés a google desde tu computadora?

import os
hostname = "google.com"
response = os.system("ping -c 1 " + hostname)
#No puedo saber, me tira "Acceso denegado. La opción -c requiere privilegios administrativos."

#Desafio X
#¿Qué devolverá la página principal (home) de nuestro sitio? Averiguá el Content-Type de /home

r = requests.get("https://macowins-server.herokuapp.com/home")
print(r.headers)
#Devuelve text/html

#Desafio XI
#consultá 4 sitios diferentes y averiguá para todos ellos qué servidor utilizan, si el contenido se transfiere encriptado, y la fecha de expieración del contenido.
a=requests.get("https://macowins-server.herokuapp.com")
b= "otra url"
c= "otra url"
d= "otra url"
#hacer un print(x.headers) para cada uno y ver los servers

#Desafio XII
#¿qué código de estado devuelve cuando un recurso es creado? Averigualo
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
print(r.status_code)
#Devuelve Status Code 201 (indicates that a new resource has been created)

#Desafio XIII
#Creá una venta.

r= requests.post('https://macowins-server.herokuapp.com/ventas')

#Desafio XIV
#Intentá hacer POST sobre una venta concreta, como por ejemplo https://macowins-server.herokuapp.com/prendas/1. ¿Qué sucede?
data = {'id': 21}
r=requests.post("https://macowins-server.herokuapp.com/prendas/1", data=data)
