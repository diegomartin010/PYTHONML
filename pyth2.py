import numpy
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

numpy.random.seed(2)

x = [1,2,3,4,5]
y = [10,20,30,40,50]

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

r2 = r2_score(train_y, mymodel(train_x))

print(r2)
print(mymodel(20))
print(mymodel)

myline = numpy.linspace(0, 100, 100)

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()