import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('salarios.csv')

print("Cantidad de datos:", dataset.shape)

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

print("x:", x)
print("y:", y)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

viz_train = plt
viz_train.scatter(X_train, Y_train, color='blue')
viz_train.plot(X_train, regressor.predict(X_train), color='black')
viz_train.title('Salario vs Experiencia')
viz_train.xlabel('Experencia')
viz_train.ylabel('Salario')
viz_train.show()

viz_train = plt
viz_train.scatter(X_test, Y_test, color='red')
viz_train.plot(X_train, regressor.predict(X_train), color='black')
viz_train.title('Salario vs Experiencia')
viz_train.xlabel('Experencia')
viz_train.ylabel('Salario')
viz_train.show()

print("Medir resultados: ",regressor.score(X_test, Y_test))