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

#Modificar la clase **Golondrina** vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este estado se alcanza cuando la energía se encuentra entre 150 y 300.

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
#Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o Jeuna golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos.
#Se propone:

#* implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

#* comprobar el código que se escribió con esta secuencia:
	#* definir un ornitólogo, dos golondrinas y dos gorriones,
	#* inicializar las aves con valores conocidos,
	#* decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
	#* decirle al ornitólogo que realice su rutina sobre aves,
	#* verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.

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
    def __init__(self,grAc,kmAc,energia):
        self.energia = energia
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
    def equilibrio(self):
        return 150 < self.energia < 300

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
        return [self.lista_aves[i].equilibrio() for i in range(len(self.lista_aves))]

pepita = Golondrina(100)
pepito = Golondrina(200)
roberto = Gorrion(100,0,200)
roberta =Gorrion(200,0,100)
pepe=Ornitologo()
pepe.estudiarAve(pepita)
pepe.estudiarAve(roberto)
pepe.estudiarAve(roberta)
pepe.estaEnEquilibrio()
pepe.realizarRutinaSobreAves()
pepita.energia
pepito.energia
roberta.grAc
roberta.kmAc
roberto.grAc
roberto.kmAc


##### **Ejercicio 4**

#Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:
#* comienzan con una cantidad que podemos establecer de _combustible_
#* los autos pueden llevar 5 personas como máximo y al _recorrer_ una distancia consumen medio litro de _combustible_ por cada kilómetro recorrido
#* las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;
#* pueden *cargar_combustible* en la cantidad que digamos y al hacerlo suben su cantidad de _combustible_
#* saben responder si _entran_ una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.
#Definí las clases **Moto**, **Auto** y **MedioDeTransporte** y hace que las dos primeras hereden de la tercera.

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



