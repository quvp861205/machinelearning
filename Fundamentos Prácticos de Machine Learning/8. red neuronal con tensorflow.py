import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_image, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
print("train_image.shape",train_image.shape)

plt.figure()
plt.imshow(train_image[100])
plt.grid(True)
plt.show()

train_images = train_image / 255.0
test_images = test_images / 255.0
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid('off')
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

#Crear modelo secuencial:
model = keras.Sequential([keras.layers.Flatten(input_shape = (28, 28)), keras.layers.Dense(128, activation = tf.nn.relu), keras.layers.Dense(10, activation = tf.nn.softmax)])

#Compilación del modelo:
model.compile(optimizer = tf.optimizers.Adam(), loss = 'binary_crossentropy', metrics = ['accuracy'])

#Entrenamiento:
model.fit(train_images, train_labels, epochs = 5)

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("Accuracy:",test_acc)

#Predicción del modelo:
predictions = model.predict(test_images)

plt.figure(figsize=(10,10))

for i in range(25):
    plt.subplot(5, 5, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.grid('off')
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    true_label = test_labels[i]
    if predicted_label == true_label:
        colorText = 'blue'
    else:
        colorText = 'red'
    plt.xlabel('{} ({})'.format(class_names[predicted_label], class_names[true_label]), color=colorText)

plt.show()