import PIL.ImageShow
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image as im

ima=im.open('D:/sunday.tif')
ima=np.array(ima)

[h,w,k]=ima.shape
#print(h,w,k)

ima=ima.reshape(-1,3)
estimator=KMeans(n_clusters=2)
estimator.fit(ima)
res=estimator.predict(ima)
#print(res)

cen=estimator.cluster_centers_
cen=np.uint8(cen)
#print(cen)

result=cen[res]
#print(result)
result.shape
result=result.reshape([h,w,3])
plt.imshow(result[:,:,1],cmap='gray')
plt.show()