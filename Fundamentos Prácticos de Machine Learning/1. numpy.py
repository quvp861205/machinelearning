import numpy as np

#NUMPY permite agilizar el uso de arrays

print( "np.array:", np.array([10, 20, 30 ,40 ,50]) )

a = np.array([10,15,89,70,36,45])
print("indice fijo:", a[4] )
print("desde un indice hasta el final:", a[3:] )
print("desde un indice a otro:", a[3:7] )
print("desde un indice en saltos de 4:", a[0::4] )
print("arrays 0:", np.zeros(5) )
print("matriz de 0 (4,5)", np.zeros((4,5)) )
print("matriz de 1 (3,5):", np.ones((3,5)) )

print("mostrar el tipo:", type(np.ones(3)))

print("numeros decimales aleatorios", np.linspace(3, 10, 5))

b = np.array( [['x','y','z'],['a','b','c']] )
print("matriz 2 dimensiones:",b)
print("numero de dimensiones:",b.ndim)

c = [12, 4, 10, 40, 2]
print("array ordenado:", np.sort(c))

cabecera = [('nombre','S10'), ('edad', int)]
datos = [('Juan',70), ('Maria',45), ('Javier', 10)]
usuarios = np.array(datos, dtype=cabecera)
print("ordenar array de objetos:",np.sort(usuarios, order='edad'))

print("Generar array con numeros consecutivos:",np.arange(5,30))

print("Generar array con numeros consecutivos de 5 en 5: ", np.arange(5,6,7) )

print("llenar matriz con un numero:", np.full((3,5),10))

print("generar matriz con una diagonal de numeros:", np.diag([1,3,9,10]))
