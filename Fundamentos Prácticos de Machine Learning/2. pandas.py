import pandas as pd

series = pd.Series( [5, 10, 15, 20, 30])
print("Series:", series)

print("Series indice 3:", series[3])

cad = pd.Series( ['A','B','C','D'] )
print("Caracteres:", cad)

lst = ['Hola','mundo','robotico']
df =  pd.DataFrame(lst)
print("dataframe:", df)

data = {
    'Nombre': ['Juan','Ana','Jose','Arturo'],
    'Edad': [14, 15, 20, 25],
    'Pais': ['mx', 'mx', 'usa', 'esp']
}
df = pd.DataFrame(data)
print("json to dataframe:", df)

print('Dataframe por columnas:', df[['Nombre','Pais']])

data = pd.read_csv('canciones.csv')
print("canciones.scv:",data.head(5))

artist = data.artists
print("artista:", artist[5])

info = data.iloc[15]
print("info artist:", info)


print("canciones ultimos registros", data.tail())

print("forma de la tabla:", data.shape)

print("columnas disponibles:", data.columns)

print("info de tempo", data["tempo"].describe())

print("ordenar:", data.sort_index(axis=0, ascending=False))

subset = data[['name','tempo','duration_ms']]
subset.sort_values(by='tempo',axis=0 , ascending=True)
print("ordenar y mostrar 3 columnas:", subset)