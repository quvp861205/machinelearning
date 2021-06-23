import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
#Data
from mnist import MNIST


mndata = MNIST('MNIST_data')
datos, labels = mndata.load_training()

plt.gray()


for i in range(25):
    plt.subplot(5,5,i+1)
    
    d_image = datos[i]
    d_image = np.array(d_image, dtype='float')
    
    pixels = d_image.reshape((28, 28))
    
    plt.imshow(pixels, cmap='gray')
    plt.title(labels[i])
    #plt.axis('o`f`f`')
plt.show()

#dividir los datos en 70% entrenamiento y 30% pruebas
from sklearn.model_selection import train_test_split
train_data, test_data, train_labels, test_labels = train_test_split(datos, labels, test_size=0.3, random_state=42)

#clasificador de arbol de decisiones
from sklearn.tree import DecisionTreeClassifier
clf_dt = DecisionTreeClassifier()

#entrenamiento con los datos de entrenamiento
clf_dt.fit(train_data, train_labels)