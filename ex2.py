# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:46:20 2021

@author: T30518
"""


import numpy as np 
import matplotlib.pyplot as plt
X = [[6], [8], [10], [14], [18]]    #pizza大小
y = [[7], [9], [13], [17.5], [18]]   #pizza價格

X2 = [[1], [10], [14], [25]] 
y2 = reg.predict(X2) 
print(y2) #繪製線性迴歸圖形 
plt.figure() 
plt.title(u'PizzaPrice with diameter.')   #標題 
plt.xlabel(u'diameter')              #x軸座標 
plt.ylabel(u'price')                  #y軸座標 
plt.axis([0, 25, 0, 25])             #區間 
plt.grid(True)                       #顯示網格 
plt.plot(X, y, 'k.')                 #繪製訓練資料集散點圖 plt.plot(X2, y2, '-g.')              #繪製預測資料集直線
plt.plot(X2, y2, '-g.')            # #繪製預測資料集直線


#plt.figure() 
#plt.title('Pizza Price with diameter.') 
#plt.xlabel('diameter(inch)') 
#plt.ylabel('price($)') 
#plt.axis([0, 25, 0, 25])  #區間
#plt.grid(True)   #顯示網格or not
#plt.plot(X, y, 'b.') 
plt.show()
