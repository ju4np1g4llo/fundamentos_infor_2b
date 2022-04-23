
>
> 🧗‍♀️ Desafío I: Creá un archivo de prueba (`bio.txt`) en la carpeta destinada a los prácticos de la materia.
>
```
with open("bio.txt", "w") as f:
     f.write("bio")
```

>
> 🧗‍♀️ Desafío II: Investigá sobre los métodos ```os.mkdir()``` y ```os.listdir()```
>
```
mkdir: crea un directorio (carpeta) en tu path actual
listdir : genera una lista de todo lo que contenga el directorio actual
```

>
> 🧗‍♀️ Desafío III: Abrí el archivo `bio.txt` y escribí una mini biografía de presentación.
> Para pensar 🤔:¿Cómo darías formato al texto que estas creando?
>
```
with open("bio.txt", "w") as f:
     f.write("Biografia de presentacion")
```


>
> 🧗‍♀️Desafio IV: Descargá el archivo [`manipulacion_archivos.txt`](https://github.com/AJVelezRueda/UCEMA_Fundamentos_de_informatica/blob/master/Python_intro/manipulacion_archivos.txt) y creá un programa que lea su contenido y lo imprima en pantalla el resultado.

```
def analisis():                                    
    with open("manipulacion_archivos.txt", "r") as f:
        print(f.readlines())                   
```
>
>
