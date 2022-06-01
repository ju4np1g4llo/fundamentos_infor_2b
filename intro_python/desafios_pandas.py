import pandas as pd
#una_serie = pd.Series(['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], dtype='string')
#print(una_serie)

#paises_latam = pd.DataFrame(data ={"Pais": ['Peru', 'Argentina', 'Bolivia', 'Uruguay', 'Brasil', 'Chile'], "Lengua oficial primaria": ['Español', 'Español', 'Español', 'Español', 'Portugues', 'Español']}, index = [1,2,3,4,5,6])
#print(paises_latam)

personas = pd.read_csv(r"C:\Users\juanp\Desktop\personas_2011.csv", sep=";")
#print(personas.head())
#print(personas.info())
#print(personas.describe())
#print(personas["edad"].median())
#print(personas["edad"].mean())

#Desafio I
#sep sirve para separar el archivo de la forma en la que quieras entre comillas (arriba se ve)
#index_col
#nrows
#header: devuelve las primeras 5 filas del df por default

#Desafio II
#read_csv
#tiene una separacion por punto y coma
#los datos estan separados

#Desafio III (desafio IV en la guia, mal enumerada)
#print(personas["seniority_level"].count())
#print(personas.groupby("seniority_level").count())
#print(personas.groupby("seniority_level")[["persona_id"]].count())

#Desafio IV (primer desafio V que aparece, hay 2 V)
#el primero te da la suma de todos los niveles
#el segundo te devuelve el dataframe ordenado por el seniority level
#el tercero te devuelve el dataframe ordenado por seniority level pero solo la columna de las personas

#Desafio V 
#print(personas["edad"]*2)     #duplica la edad de todos los valores en la serie
#print(personas["edad"])
#print(personas["edad"]+2)      #le suma 2 a todos los valores de la serie
#print(personas["edad"]>2)      #te retorna un booleano

#Desafio VI

#print(personas.groupby("anio")[["edad"]].count())
#treinta = personas.loc[personas["edad"]==30]
#print(treinta.groupby("anio").count())

#Desafio VII

categorias = pd.read_csv(r"C:\Users\juanp\Desktop\ref_categoria_conicet.csv", sep=";")

print(categorias.columns)
print(personas.columns)
#tienen en comun la columna categoria_conicet_idc