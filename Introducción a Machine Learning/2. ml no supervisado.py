# importar las librerias para los graficos
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

# importar manejo de array
import numpy as np

# importar el generador de ejemplos
from sklearn.datasets import make_blobs


#graficarlo
X, Y = make_blobs(n_samples=500, centers=4)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()

# importamos el KMeans para el agrupamiento
from sklearn.cluster import KMeans

# indicamos el numero de agrupamientos
kMeans = KMeans(n_clusters=4)

# entrenamos el algoritmo con los datos anteriores
kMeans.fit(X)

# luego de entrenar usamos la prediccion
y_kMeans = kMeans.predict(X)

# nos devuelve los puntos centrales donde estan las agrupaciones
centers = kMeans.cluster_centers_
print("centros encontrados por kmeans:",centers)

# graficamos los puntos agrupados en colores diferentes
plt.scatter(X[:, 0], X[:, 1], c=y_kMeans, cmap='viridis')

# incluimos los centroides
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
plt.show()