


>
> 🧗‍♀️ Desafío VI: Después de tanto programar necesitamos unos matecitos. Hoy aprendiste a prepararlos. Lo que no estoy segura es de que el agua alcance para toda la ronda. Suponiendo que cada cebada de mate consume del 30 ml de agua. Cosntruí una función que nos permita calcular cuántos termos de 1000 ml llenos consumiremos para un ronda dada (es decir una cantidad de personas dada).

    def mates(rondas,personas):
        agua_gastada_ronda = personas * 30 
        agua_gastada_total = agua_gastada_ronda * rondas
        return agua_gastada_total
>
>
> 🧗‍♀️ Desafío VII: Siempre con los mates, vienen bien unas facturitas 🥐🥐
>
>¿Si hacemos una `vaquita` ? _Vaquita_ se le dice en Argentina a hacer una colecta de plata para un fin común. Creá función que nos permita dividir los costos de una docena de facturas entre cierta cantidad de comensales.
>
    docena = 250
    def facturas(personas):
     por_persona = docena/personas
     return por_persona





>
> 🧗‍♀️ Desafío VIII: En una ronda pequña de mate 🧉 no hace falta llenar tooooodo el termo, con un poco de agua quizás alcanza. Definí una función _calcular_cantidad_de_agua_ que espere una cantidad de personas como argumento y devuelva la cantidad de mililitros con los que tenemos que cargar el termo. 
>
>👀  ¡OJO!  Si llega a 1000 debería retornar la advertencia `"vas a necesitar más de un térmo"`

    def calcular_cantidad_de_agua(personas):
        agua_usada = personas * 30
        if agua_usada > 1000:
             print("Vas a necesitar mas de un termo")
        else:
             return agua_usada



