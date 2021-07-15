A continuación, mostramos como utilizar scikitlearn con los diferentes algoritmos descritos:


Regresión Lineal De tipo: Regresión

    from sklearn import linear_model


Regresión Logística De tipo: Clasificación
    
    from sklearn.linear_model import LogisticRegression


Naïve Bayes De tipo: Clasificación
    
    from sklearn.naive_bayes import GaussianNB


k-Nearest Neighbors De tipo: Regresión, Clasificación
    
    from sklearn.neighbors import KNeighborsClassifier


Decision Tree – Arbol de Decisiones De tipo: Clasificación y Regresión

    from sklearn import tree
    tree.DecisionTreeRegressor()
    tree.DecisionTreeClassifier()


Random Forest
De tipo: Regresión y clasificación

    from skelarn.ensemble import RandomForestRegressor
    from skelarn.ensemble import RandomForestClassifier 
    Scikit-Learn Machine Learning No Supervisado
    k-means
    from sklearn.cluster import KMeans


Scikit-Learn Set de Datos
    
    sklearn.datasets
    from sklearn.datasets import load_iris-> clasificación de flores


Otros data sets:
    
    - california_housing: para regresión de valor de precios de casas
    - load_breast_cancer:para clasificación de células cancerígenas
    - Y existen varios tipos más para aplicar machine learning supervisado a clasificación y regresión.


Además de los set de datos listos para trabajar, existe el generador de ejemplos (“sample generators”) por ejemplo:
    
    make_blobs, utilizado en uno de los ejemplos del curso.
    from sklearn.datasets.samples_generator import make_blobs


scikit-Learn Metrics
    
    Para evaluar nuestro modelo entrenado, scikit-learn cuenta con diferentes métricas que nos permite estimar el rendimiento del algoritmo seleccionado.


Como las que usamos en el proyecto, como ser:
    
Matriz de confusión:

    from sklearn.metrics import confusion_matrix
