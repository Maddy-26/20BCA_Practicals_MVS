# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:53:12 2022

@author: Madhavan
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data1=pd.read_csv('heart.csv')
print(data1.head())
print(data1.describe())
sns.countplot(x ='sex', data= data1)
plt.show()
sns.scatterplot(x ='age',y ='trestbps',hue='sex',data =data1)
plt.show()
sns.pairplot(data1.drop(['Id'],axis=1),hue='sex',height=3)
plt.show()
X=data1.corr(method='pearson')
print(X)
sns.heatmap(data1.corr(method='pearson').drop(['Id'],axis=1).drop(['Id'],axis=0))
plt.show()
sns.boxplot(x="sex",y="trestbps",data=data1)
plt.show()

