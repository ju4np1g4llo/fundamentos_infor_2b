

>
> 🧗‍♀️Desafio I: Descargá y ejecutá el [`script1_manejo_errores.py`](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/script1_manejo_errores.py)
>
> Para pensar 🤔: ¿Qué tipo de error se obtiene al ejecutar el programa? ¿En dónde se encuentra el error? ¿Cómo te das cuenta? 
>
```
Aparece un Syntax Error que dice que falto cerrarse un parentesis. Te dice donde esta el error mediante esta flecha ^ por debajo del lugar donde esta el error
```


>
> 🧗‍♀️Desafio II: Creá una función denominada _mitades_ que tenga como argumento un número e imprima el resultado de la división de ese número por 2
```
def mitades(n):  
  print(n/2)
  ```
>
>Para pensar 🤔: ¿Qué crees que ocurrirá cuando ingresas un 9 como parámetro? ¿Y con un 0?
```
No me tira ningun error ¿? (Division de 9/2 = 4.5 y 0/2 = 0.0)
```
>
> 🧗‍♀️Desafio III: ¿Cómo mejorarías tu función para que sea capaz de manejar el error de la división por cero? Reescribí la función incorporando una declaración try-except
>
```
def mitades0(n):
    try:
      print(n/0)
    except:
      print("Hay un error")
```
