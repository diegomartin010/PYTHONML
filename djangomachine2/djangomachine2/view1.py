from django.http import HttpResponse
import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import pickle


def index(request):
    print('Holaaanda')
    filename = 'finalized_model.sav'
    dtree = pickle.load(open(filename, 'rb'))
    
    orden = request.GET.get('orden')
    cliente = request.GET.get('cliente')
    diasFab = request.GET.get('diasFab')
    maquina = request.GET.get('maquina')
    #array1 = [[8001, 0, 5, 40]]
    array1 = [[orden, cliente, diasFab, maquina]]
    print(array1)

    prediccion = dtree.predict(array1)
    print(prediccion)
    return HttpResponse(prediccion)

def elcapo(request):
    return HttpResponse("soyelcapo")