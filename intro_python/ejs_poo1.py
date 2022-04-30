
##### **Ejercicio 1**

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2

#INTERFAZ: energia, comer, acariciar, estaDebil
#ESTADO: alimento, caricias

##### **Ejercicio 2**


def volar(self, kms):
    if self.energia > 0:
        self.energia -= 10 + kms

##### **Ejercicio 3**

class Notebook():
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    def descuento(self,descuento):
        self.descuento = self.precio - (descuento/100)*self.precio
        print(self.descuento)
        

##### **Ejercicio 4**

class Contador():
    def __init__(self,segundos):
        self.valorActual = segundos
    def inc(self):
        self.valorActual += 1
    def dis(self):
        self.valorActual -= 1
    def valorNuevo(self,segundos):
        self.valorActual = segundos
        self.valorNuevo = self.valorActual
    def reset(self):
        self.valorActual = 0
        
##### **Ejercicio 5**
#Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. 
#Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). 
#El método para saber el último comando es `ultimoComando`, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador():
    def __init__(self,segundos):
        self.valorActual = segundos
    def inc(self):
        self.valorActual += 1
    def dis(self):
        self.valorActual -= 1
    def valorNuevo(self,segundos):
        self.valorActual = segundos
        self.valorNuevo = self.valorActual
    def ultimoComando(self):
        
        
##### **Ejercicio 6**
class Calculadora:
    def __init__(self):
        self.calculadora = self
    def cargar(self,numero):
        self.valorActual = numero
    def sumar(self,numero):
        self.valorActual += numero
    def restar(self,numero):
        self.valorActual -= numero
    def multiplicar(self,numero):
        self.valorActual *= numero

##### **Ejercicio 7**

class Gorrion:
    def __init__(self,grAc,kmAc):
        self.grAc= grAc
        self.kmAc= kmAc
        self.liGr=[] 
        self.liKm=[]
    def comer(self, gr): 
        self.liGr.append(gr) 
        self.grAc+=gr 
    def volar(self, kms): 
        self.liKm.append.appen(kms)
        self.kmAc+=kms
    def css(self):                     
        if self.grAc >0:
            return self.kmAc/self.grAc
        else:
            return None
    def cssp(self):
        if self.grAc >0:
            return max(self.liKm)/max(self.liGr)
        else:
            return None
    def cssv(self):
        if self.grAc >0:
            return len(self.liKm)/len(self.liGr)
        else:
            return None
    def enEq(self):
        return 0.5 <= self.css() <=2


pepita = Gorrion(70, 50)

print(pepita.enEq())