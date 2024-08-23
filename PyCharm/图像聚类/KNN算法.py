import matplotlib.colors
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris

iris=load_iris()
x=iris.data[:,:2]
y=iris.target
print(iris.feature_names)
cmap_light=matplotlib.colors.ListedColormap(['#FFAAAA','#AAFFAA','#AAAAFF'])
cmap_bold=matplotlib.colors.ListedColormap(['#FF0000','#00FF00','#0000FF'])
clf=KNeighborsClassifier(n_neighbors=10,weights='uniform')
clf=clf.fit(x,y)
x_min,x_max=x[:,0].min()-1,x[:,0].max()+1
y_min,y_max=x[:,1].min()-1,x[:,1].max()+1
xx,yy=np.meshgrid(np.arange(x_min,x_max,0.02),np.arange(y_min,y_max,0.02))
z=clf.predict(np.c_[xx.ravel(),yy.ravel()]).reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,z,cmap=cmap_light)
plt.scatter(x[:,0],x[:,1],c=y,cmap=cmap_bold)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()
