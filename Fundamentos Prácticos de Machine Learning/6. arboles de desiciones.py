import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split

sns.set()

test_df = pd.read_csv('titanic-test.csv')
train_df = pd.read_csv('titanic-train.csv')
print("Primeros registros:",train_df.head())

train_df.Sex.value_counts().plot(kind='bar', color=['b','r'])
plt.title("Distribucion de sobrevivientes")
plt.show()

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()

#VAMOS A REALIZAR EL LIMPIADO DE LA TABLA

# convertir labeles a numeros
encoder_sex = label_encoder.fit_transform(train_df['Sex'])
print("nueva modificacion a la tabla:",train_df.head())

#reemplazar age datos vacios en la media de age
train_df['Age'] = train_df['Age'].fillna(train_df['Age'].median())
#reemplazar emarked datos vacios con s
train_df['Embarked'] = train_df['Embarked'].fillna('S')

#eliminar datos que no son utiles
train_predictors = train_df.drop(['PassengerId', 'Survived', 'Name', 'Ticket', 'Cabin'], axis=1)

#obtener variables categoricas
categorical_cols = [cname for cname in train_predictors.columns if train_predictors[cname].nunique()<10 and train_predictors[cname].dtype=='object']
print("categorical_cols:", categorical_cols)

#obtener variables numericas
numeric_cols = [cname for cname in train_predictors.columns if train_predictors[cname].dtype in ['int64', 'float']]
print("numeric_cols:", numeric_cols)

#juntar las variables categoricas con las numericas
my_cols = categorical_cols + numeric_cols

train_predictors = train_predictors[my_cols]

#permite generar informacion aleatoria
dummy_encoded_train_predictors = pd.get_dummies(train_predictors)
print("dummy_encoded_train_predictors:", dummy_encoded_train_predictors.head())
print("como dividio los datos:",train_df['Pclass'].value_counts())

"""

    algunas cosas que comentar que pueden ser utiles

    > cuando se hace el drop intentando eliminar algunas variables que no serán de interés, axis = 1 
      indica que estas variables son "columnas ", axis = 0 , indicaría que son filas.
    > las dummy variables que se mencionan ligeramente convierten las variables categóricas 
      en indicadoras como 0,1,2,…etc
    > uando se completaron los valores faltantes en las variables edad y la clase del 
      pasajero (embarked), faltó mencionar un comando muy util para saber en que variables se 
      tienen valores faltantes. Se puede usar train_df.isnull.any().

"""

y_target = train_df['Survived'].values
x_features_one = dummy_encoded_train_predictors.values
X_train, X_validation, Y_train, Y_validation = train_test_split(x_features_one, y_target, test_size=.25, random_state=1)

tree_one = tree.DecisionTreeClassifier()
tree_one = tree_one.fit(x_features_one, y_target)

tree_one_accuracy = round(tree_one.score(x_features_one, y_target), 4)
print("Accuracy: %0.4f" %(tree_one_accuracy))

from io import StringIO
from IPython.display import  Image, display
import pydotplus

out = StringIO()
tree.export_graphviz(tree_one, out_file=out)
graph = pydotplus.graph_from_dot_data(out.getvalue())
graph.write_png('./titanic.png')
