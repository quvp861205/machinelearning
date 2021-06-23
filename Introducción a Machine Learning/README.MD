Datasets de ejemplo: http://yann.lecun.com/exdb/mnist/
(Contiene mas de 60000 ejemplos de digitos escritos a mano)

Otros datasets:
	https://www.kaggle.com/datasets



- Para el trabajo con listas de datos: NumPy
- Para hacer las gráficas: Matplotlib
- Para seleccionar el modelo de aprendizaje de Machine Learning: Scikit-Learn


**instalar librerias**

- pip install numpy
- pip install matploitlib
- pip install sklearn
- pip install -U scikit-learn
- pip install python-mnist
- pip install seaborn

---------------------------------

Machine Learning Supervisado Algoritmos: Regresión Lineal, Logísticay Naive Bayes

  - **Regresión Lineal:** Es uno de los más conocidos en Estadística y Machine Learning: Busca una relación lineal entre las diferentes variables, debemos recordar que dentro de este algoritmo tenemos valores numéricos por lo que estamos hablando de un problema de regresión o predicción. La Regresión Lineal nos ayuda a predecir el siguiente valor numérico.

  - **Regresión Logística:** Nos permite ver los valores categóricos, una clasificación como un cero y un uno. Para encontrar los valores con las variables independientes se utiliza la estimación de Maximun Likelihood o la máxima verosimilitud.

  - **Naives Bayes:** Este algoritmo es específicamente para clasificación, como cuando queremos clasificar los emails que nos llegan y cuáles de ellos son spam.


Machine Learning Supervisado Algoritmos: K-Nearest Neighbors, Decision Tree, Random Forest, y Redes Neuronales

  - **K-nearest neighbors:** Este algo nos sirve para predecir un valor numérico y clasificar un valor categórico. Trabaja directamente con toda el set de datos de entrenamiento, si tengo un K igual a tres o cinco eso será el número de vecinos cercanos y para saber cuáles están más cerca podemos usar los tipos de distancias como Euclidiana, Hamming, Manhattan.

  - **Decision Tree:** Este tipo de algoritmo también nos sirve para predecir y clasificar, se basa en las decisiones. Si queremos tomar decisiones sobre los puntos mayores o menores empezamos a dividir dependiendo de nuestras decisiones.

  - Es importante considerar dos puntos principales: El Indice Gini y la ganancia de información, el primero trabajo con los atributos de valores continuos y es una función para medir el grado de impureza de nodos en nuestro árbol de decisiones para saber que tan mezclados y desordenados están; el segundo está relacionado a los atributos categóricos, es un criterio para estimar la información, estimamos la información que aporta cada atributo a sobre todo nuestro set de datos.

  - **Random Forest:** Todo lo estudiado en el árbol de decisiones nos sirve en este tipo de algoritmo, nos permite la predicción de valores numéricos y categóricos. También se le denomina Ensamble, puede trabajar con un grupo de algoritmos.

  - **Redes Neuronales:** Nos sirve también para hacer las predicciones y clasificaciones.

-----------------------

Ahora nos vamos a enfocar en los tipos de datos que no tienen etiquetas y entran en la categoria de Machine Learning No Supervisado, esto no servirá para realizar el agrupamiento de los datos(Clustering) o para hacer la reducción de dimensionalidad por si tenemos muchos datos.


**K-Means:** K también significa los números que vamos a utilizar en nuestro Clusters. Imagina que tenemos un grupo de datos y queremos agruparlos por su similitud. Cada grupo va a tener un centro y a partir de ahí se agrupan todos los demás con características parecidas. Se tienen tanto el K-grupos y Centroide.
- K: cuantas agrupaciones queremos encontrar en los datos
  
------------------------------

**Evaluando nuestro algoritmo entrenado**


Necesitamos verificar si realmente el algoritmo está aprendiendo las características que le estamos dando a la entrada para que nos de respuestas exactas en la salida. Es importante separar este concepto de aprender de lo que es memorizar, cuando un algoritmo empieza a memorizar no va a saber que colocar en la salida.


- **Overfitting:** Nuestro algoritmo esta aprendiendo muy bien los datos de entrenamiento, se ha puesto a memorizar.
- **Underfitting:** El algoritmo no esta aprendiendo.


Algunos métodos de evaluación:

- Matriz de evaluación
- Score/Puntuación
- Validación Cruzada/Cross Validation
- Algoritmos de prueba
- Area Under the Cure(AUC)

----------------------------------

**La matriz de confusión** nos ayuda a visualizar aquellos valores de predicción de salida del algoritmo y por otro lado los valores reales según nuestras etiquetas. En una matriz de confusión podemos ver los valores bien clasificados, como el verdadero positivo, falso positivo, falso negativo y verdadero negativo.


Otros valores que nos permiten ver qué tan bien entrenado esta nuestro algoritmo, estos son precisión y recall.

- **Precisión:** Acá consideramos los verdaderos positivos y los falsos positivos.
- **Recall:** Acá consideramos los verdaderos positivos y los falsos negativos.

-------------------------

Para convertirte en un profesional en Machine Learning necesitas conocer sobre:

- Álgebra Lineal
- Probabilidad y Estadística
- Cálculo



El Álgebra Lineal es importante en el Machine Learning porque necesitamos entender los conceptos básicos que van por detrás de los algoritmos.

   Algunos temas a saber son:

    - Regresión Lineal
    - Regresión de Mínimos Cuadrados
    - Matrices


- 1- Regresión Lineal: Cuando tenemos valores incógnitos que relacionan directamente dos variables.
- 2- Regresión de Mínimos Cuadrados: Para encontrar la eficiencia en el rendimiento de nuestro algorítmo entrenado.
- 3- Matrices: Las hemos utilizado en la matriz de confunsión. Si utilizamos técnicas de machine learning más avanzadas vamos a representar, por ejemplo, a las imagenes de los números escritos a mano en una matriz.

--------------------

Conceptos de la Probabilidad y Estadística utilizados en el Machine Learning:

	● Estadística:
		1- Inferencia / Descriptiva: Nos ayuda a entender todos los grupos de datos que tenemos.
		2- Varianza: La utilizamos a la hora de probar el rendimiento de nuestro algorítmo, la diferencia entre los datos de predicción y los datos reales en el Machine Learning Supervisado.
		3- MLE (Maximum Likelihood Estimation): Para conocer como trabajar minimizando los errores de nuestro algorítmo.

	● Probabilidad:
		1- Probabilidad Condicional
		2- Teorema de Bayes: Es la base del clasificador Naive Bayes.
		3- Variables aleatorias: Para entender el comportamiento de las mismas.
