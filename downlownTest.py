import numpy as np
import matplotlib.pyplot as plt
import sklearn
from sklearn import datasets
import datetime
# from sklearn import svm

iris = datasets.load_iris()
print(iris.data.shape, iris.target.shape)

class_mate = ['张三', '李四', '王五']
print(type(repr(class_mate)))

x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
# plt.show()

print(dir(datetime.datetime))
print(np.eye(4))
