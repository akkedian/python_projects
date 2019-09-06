# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:00:08 2019

@author: north_ner
"""

from sklearn import datasets
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')
ir=datasets.load_iris()
type(ir)
print(ir.keys())
print(ir.data.shape)

#performing exploratoy data analysis EDA
x=ir.data 
y=ir.target
df=pd.DataFrame(x,columns=ir.feature_names)
print(df)
z=pd.plotting.scatter_matrix(df,c=y,figsize=[8,8],s=150,marker='D')

#a=z.hist()
#fig=a.get_figure()
#fig.savefig('C:\\Users\\Great\\Desktop\\python\\datascience\\figure.pdf')
f=open('iri.pdf','w')
f=z
f.close()
