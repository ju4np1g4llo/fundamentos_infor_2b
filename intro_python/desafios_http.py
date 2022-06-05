from calendar import c
from this import d
from turtle import home
import requests

r = requests.get('https://macowins-server.herokuapp.com/prendas')
#print(r.json())
#print(r.status_code)


#Desafio III 
#print(requests.get("https://macowins-server.herokuapp.com/prendas/1"))
#"<Response [200]>"

#Desafio IV
#print(requests.get("https://macowins-server.herokuapp.com/prindas/1"))
#"<Response [404]>"

#Desafio V
#print(requests.get('https://macowins-server.herokuapp.com/ventas'))
#print(requests.get('https://macowins-server.herokuapp.com/ventas/2'))
#La barra / no afecta si no tiene un numero al lado, por lo qe buscara como si no tuviese
#Los 2 te devuelven Response 200 porque puede encontrar algo

#Desafio VI
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')
#print(r.json())

#Desafio VII
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
#print(r.json())

#Desafio VIII
#Está definiendo que la URL busque el recuerdo de la clase de http de hoy en nuestro cerebro como una "pagina web"

#Desafio IX
import os
#hostname = "google.com"
#response = os.system("ping -c 1 " + hostname)
#No puedo saber, me tira "Acceso denegado. La opción -c requiere privilegios administrativos."

#Desafio X
r = requests.get("https://macowins-server.herokuapp.com/home")
#print(r.headers)
#Devuelve text/html

#Desafio XI
a=requests.get("https://macowins-server.herokuapp.com")
b
c
d
#hacer un print(x.headers) para cada uno y ver los servers
#Desafio XII
#data = {'id': 21}
#r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
#print(r.status_code)
#Devuelve Status Code 500 (Un internal server error)

#Desafio XII
#No se hacerlo

#Desafio XIII
