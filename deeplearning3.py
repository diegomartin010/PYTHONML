import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pickle

# load the model from disk
filename = 'finalized_model.sav'
dtree = pickle.load(open(filename, 'rb'))

array1 = [[8001, 0, 5, 40]]
array2 = [[8001, 1, 7, 40]]
array3 = [[8002, 1, 7, 40]]
array4 = [[8003, 1, 7, 40]]

print(dtree.predict(array1))
print(dtree.predict(array2))
print(dtree.predict(array3))
print(dtree.predict(array4))
