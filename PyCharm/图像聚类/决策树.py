import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split

iris=load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.20,random_state=20)

clf=tree.DecisionTreeClassifier()
clf=clf.fit(x_train,y_train)
plt.figure(dpi=200)
tree.plot_tree(clf,feature_names=iris.feature_names,class_names=iris.target_names)

print('数据[6,5,5,2]的类别:',clf.predict([[6,5,5,2]]))
print('数据的标签：\n',y_test)
print('模型的准确率：',"{0:.3f}".format(clf.score(x_test,y_test)))