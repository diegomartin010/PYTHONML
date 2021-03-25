import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pickle

dataset = pandas.read_csv("DATAMACHINELEARNING.csv")
clientes = {'Aramco': 0, 'YPF': 1}
dataset['Cliente'] = dataset['Cliente'].map({'Aramco': 0, 'YPF': 1})
print(dataset)

training = dataset[['Producto','Cliente', 'Dias Fab', 'Performance Linea']]
result = dataset[['Score Escenario']]
print(training)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(training, result)

filename = 'finalized_model.sav'
pickle.dump(dtree, open(filename, 'wb'))

print(dtree.score(training,result))
 

array = [[8003, 0, 7, 40]]

print(dtree.predict(array))
print(dtree.predict(array))
print(dtree.predict(array))
print(dtree.predict(array))
