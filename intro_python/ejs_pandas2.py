
##### **Ejercicio 1**
import pandas as pd
#Escribí un programa que dado un diccionario cuyos valores sean listas de números cree un DataFrame y luego seleccione e imprima las filas del DataFrame basado en un valor de una columna.
dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(dato)
print(df.loc[df[1]==4])


##### **Ejercicio 2**
#Escribí un programa que guarde en una lista una columna de un DataFrame.
print(df[1].to_list())

##### **Ejercicio 3**
#Realizá un programa que agregue datos a un DataFrame vacío.

dfVac = pd.DataFrame()
s1 = pd.Series([1,4,3,4,5])
df = dfVac.append(s1, ignore_index=True)
print(df)

##### **Ejercicio 4**

#quiero eliminar las primeras 2 filas
df1 = df.loc[2:]
print(df1)

##### **Ejercicio 5*
# Realizá un programa que verifique si una columna dada se encuentra presente en un DataFrame.*

dato = {1: [1, 4, 3, 4, 5], 2: [4, 5, 6, 7, 8], 3: [7, 8, 9, 0, 1]}
df = pd.DataFrame(dato)
print(df.columns)
if 3 in df.columns:
    print("si")
else:
    print("no")

##### **Ejercicio 6**
#Escribí un programa que dado dos diccionarios genere dos DataFrame y los una tanto en el eje de las columnas como en el eje de las filas.

##### **Ejercicio 7**
#Creá un programa que dado un diccionario y una lista añada está última al DataFrame generado a partir del diccionario.

##### **Ejercicio 8**
#Realizá un programa que dado dos DataFrames genere otro que contenga solo las columnas en común.
