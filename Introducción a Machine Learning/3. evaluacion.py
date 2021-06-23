# Requirements
#   pip install matplotlib
#   pip install python-mnist
#   pip install scikit-learn

import numpy as np
from matplotlib import pyplot as plt
from mnist import MNIST
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix


def evaluate_classifier(classifier, t_data, t_labels):
    prediction = classifier.predict(t_data)
    c_matrix = confusion_matrix(t_labels, prediction)
    return c_matrix


def generate_score(c_matrix):
    return (c_matrix.diagonal().sum() * 100.) / c_matrix.sum()


# define and load data from path
mnData = MNIST('MNIST_data')
data, labels = mnData.load_training()

# split data to train
train_data, test_data, train_labels, test_labels = train_test_split(data, labels, test_size=0.3, random_state=46)

# Decision Tree
dt_classifier = DecisionTreeClassifier()
dt_classifier.fit(train_data, train_labels)
cm = evaluate_classifier(dt_classifier, test_data, test_labels)
print("Clasificador decision Tree:", cm)
score = generate_score(cm)
print("Score decision tree:", score)

# Random Forest
rf_classifier = RandomForestClassifier(n_estimators=150, min_samples_split=2)
rf_classifier.fit(train_data, train_labels)
cm2 = evaluate_classifier(rf_classifier, test_data, test_labels)
print("Clasificador Random Forest:", cm2)
score2 = generate_score(cm2)
print("Score Random Forest:", score2)

# Probando nuestro algoritmo entrenado en un set de datos nuevos

#cargamos los datos de evaluacion del MNIST
test_data, test_labels =mnData.load_testing()

# aplicamos el clasificador a todo e dataset de evaluacion y obtenemos el accuracy
predicted = rf_classifier.predict(test_data)

# evaluamos los resultados con la matriz de confusion para el dataset de evaluacion
mc = evaluate_classifier(rf_classifier, test_data, np.array(test_labels))

print("MC:", mc)

#score
score = mc.diagonal().sum()*100/mc.sum()
print("Score:", score)

digitextra = test_data[7]
d = np.array(digitextra, dtype='float')
pixels = d.reshape((28,28))
plt.imshow(pixels, cmap='gray')
plt.show()

print("La red neuronal predice que es un numero: ",rf_classifier.predict([test_data[7]]))

