# **Práctica Objetos - Parte 2**

##### **Ejercicio 1**
#cuales son sus estados

#Perro: alimento, caricias
#Gato: alimento, caricias

#cuales son sus interfaces
#Perro: energia,comer,alimento,acariciar,estaDebil,pasear
#Gato: energia,comer,pasear,caricias,acariciar,estaDebil

#¿Comparten interfaz?
#No, pero entienden algunos de los mismos métodos
#¿Son polimórficas?
#No, son parcialmente polimorficas
from statistics import median_low


class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0
    def energia(self):
        return self.alimento + (self.caricias * 10)
    def comer(self, gramos):
        self.alimento += gramos
    def alimento(self):
	    print(self.alimento)
    def acariciar(self):
        self.caricias += 1
    def estaDebil(self):
        return self._caricias < 2
    def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0
    def energia(self):
        return self.alimento + (self.caricias * 8)
    def comer(self, gramos):
        self.alimento += gramos * 1.5
    def caricias(self):
	    print(self.caricias)
    def acariciar(self):
        self.caricias += 1
    def estaDebil(self):
        return self._caricias < 4


##### **Ejercicio 2**

class Golondrina:
    def __init__(self, energia):
        self.energia = energia
    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos
    def volar_en_circulos(self):
        self.volar(0)
    def volar(self, kms):
        if self.energia > 0:
            self.energia -= 10 + kms
    def equilibrio(self):
        if 150 < self.energia < 300:
            print("En equilibrio")
        else:
            print("En desequilibrio")

##### **Ejercicio 3** 

class Golondrina():
    def __init__(self, energia):
        self.energia = energia
    def comer_alpiste(self, gramos):
        self.energia += 4 * gramos
    def volar_en_circulos(self):
        self.volar(0)
    def volar(self, kms):
        if self.energia > 0:
            self.energia -= 10 + kms
    def equilibrio(self):
        return 150 < self.energia < 300

class Gorrion():
    def __init__(self,grAc,kmAc):
        self.grAc= grAc
        self.kmAc= kmAc
        self.liGr=[] 
        self.liKm=[]
    def comer_alpiste(self, gr): 
        self.liGr.append(gr) 
        self.grAc+=gr 
    def volar(self, kms): 
        self.liKm.append.appen(kms)
        self.kmAc+=kms

class Ornitologo():
    def __init__(self):
        self.lista_aves = []
    def avesEnEstudio(self):
        print(self.lista_aves)
    def estudiarAve(self,ave):
        self.lista_aves.append(ave)
    def realizarRutinaSobreAves(self):
        for ave in self.lista_aves:
            ave.comer_alpiste(80)
            ave.volar(70)
            ave.comer_alpiste(10)
        print("Rutina Realizada para todas las aves")
    def estaEnEquilibrio(self):
        for ave in self.lista_aves:
            if ave.equilibrio:
                return ave

pepita = Golondrina(100)
pepito = Golondrina(200)
roberto = Gorrion(100,0)
roberta =Gorrion(200,0)
pepe=Ornitologo()
pepe.estudiarAve(pepita)
pepe.estudiarAve(roberto)
pepe.estudiarAve(roberta)
pepe.realizarRutinaSobreAves()
pepita.energia
pepito.energia
roberta.grAc
roberta.kmAc
roberto.grAc
roberto.kmAc


##### **Ejercicio 4**
class MedioDeTransporte:
    def __init__(self,combustible):
        self.combustible = combustible
    def cargar_combustible(self,litros):
        self.combustible += litros


class Auto(MedioDeTransporte):
    def entran(self,personas):
        return personas <= 5


class Moto(MedioDeTransporte):
    def entran(self,personas):
        return personas <= 2




