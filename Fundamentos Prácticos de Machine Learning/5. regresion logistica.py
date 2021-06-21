import pandas as pd
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline

diabetes = pd.read_csv('diabetes.csv')
print("5 registros diabetes:",diabetes.head(5))
print("forma tabla:",diabetes.shape)

feature_cols = ["Pregnancies","Insulin","BMI","Age","Glucose","BloodPressure","DiabetesPedigreeFunction"]
x = diabetes[feature_cols] #necesario para saber si tiene diabetes
y = diabetes.Outcome #indicador si tiene diabetes

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.25, random_state=0)

logreg = LogisticRegression(max_iter=10000000)
logreg.fit(X_train, Y_train)
y_pred = logreg.predict(X_test)
print("Como se clasificaron los datos: (1 tiene diabetes, 0 no tiene diabetes)", y_pred)

#validar resultados con la matriz de confusion
cnf_matrix = metrics.confusion_matrix(Y_test, y_pred)
print("matriz de confusion:",cnf_matrix)

import numpy as np
class_names = [0,1]
fig, ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks, class_names)
plt.yticks(tick_marks, class_names)

sns.heatmap(pd.DataFrame(cnf_matrix), annot=True, cmap='Blues_r', fmt='g')
ax.xaxis.set_label_position('top')
plt.tight_layout()
plt.title('Matriz de confusion', y=1.1)
plt.ylabel('Etiqueta actual')
plt.xlabel('Etiqueta de prediccion')
plt.show()

"""
                               PREDICCION   
-------------------------------------------------------                    Positivos     |    Negativos
        |                Positivos     |    Negativos
        -----------------------------------------------
OBSER   | Positivos  |   Verdaderos    |    Falsos
VACION  |            |   Positivos     |    Negativos
        |-----------------------------------------------
        | Negativos  |   Falsos        |    Verdaderos
        |            |   Positivos     |    Negativos
--------------------------------------------------------


Los verdaderos positivos (VP) son aquellos que fueron clasificados correctamente como positivos como el modelo.
Los verdaderos negativos (VN) corresponden a la cantidad de negativos que fueron clasificados correctamente como negativos por el modelo.
Los falsos negativos (FN) es la cantidad de positivos que fueron clasificados incorrectamente como negativos.
Los falsos positivos (FP) indican la cantidad de negativos que fueron clasificados incorrectamente como negativos.

Un médico tiene cuatro pacientes y a cada uno se les solicitó un examen de sangre y por error el laboratorio realizó también un estudio de embarazo, cuando los pacientes llegan el médico les da los resultado.

A la primera paciente le da la noticia que está embarazada y ella ya lo sabía dado que tiene 3 meses de embarazo, es decir, un verdadero positivo.

El siguiente paciente llega y le dice que no está embarazada y es una clasificación evidente dado que es hombre (Verdadero negativo).

El tercer paciente llega y los resultados le indican que no está embarazada sin embargo tiene cuatro meses de embarazo, es decir, que la ha clasificado como falso negativo.

Y por último el cuarto paciente sus resultados han indicado que está embarazado sin embargo es hombre por lo cual es imposible, dando como resultado un falso positivo.

"""

print("Exactitud:", metrics.accuracy_score(Y_test, y_pred))
