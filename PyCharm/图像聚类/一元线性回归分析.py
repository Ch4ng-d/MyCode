import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.linear_model import LinearRegression

#导入数据集
iris=load_iris()
data=pd.DataFrame(iris.data)
data.columns=['sepal-length','sepal-width','petal-length','petal-width']

#数据处理
x=data['petal-length'].values
y=data['petal-width'].values
x=x.reshape(len(x),1)
y=y.reshape(len(y),1)

clf=LinearRegression()    #建立模型
clf.fit(x,y)           #模型学习
pre=clf.predict(x)      #预测

#将数据转化为图形
plt.scatter(x,y,s=50)   #散点图
plt.plot(x,pre,'r-',linewidth=2)
plt.xlabel('petal-length')
plt.ylabel('petal-width')
for idx,m in enumerate(x):
    plt.plot([m,m],[y[idx],pre[idx]],'g-')
plt.show()

print("系数=",clf.coef_)
print("截距=",clf.intercept_)
print('预测值为=',clf.predict([[3.9]]))