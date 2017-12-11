# -*- coding: utf-8 -*-
"""
Created on Sat Dec 02 16:01:26 2017

@author: naren
"""

import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('file_clean2.csv')
preg = preg.fillna('')

topic1= (preg.Topic == 'Alcohol Use') | (preg.Topic == 'Tobacco Use')  & (preg.Break_Out == 'Age < 18')

intersection = preg[topic1]

plot1 = intersection.groupby('LocationDesc').Topic.value_counts().unstack()

plot1.plot(kind='area', figsize=(16,6), stacked= True, colormap='summer')
plt.xlabel('State in United Sates')
plt.title('Tobacco or Alcohol consumption during pregnancy')
plt.show()