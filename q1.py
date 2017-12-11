# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:52:38 2017

@author: naren
"""
#Locationwise physical abuse during pregnancy using Tuple
import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('file_clean2.csv')
preg = preg.fillna('')



topic1= (preg.Topic == 'Abuse - Physical')

intersection = preg[topic1]
explode = (0.1, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
plot1 = intersection['LocationDesc'].value_counts()

plot1.plot.pie(figsize=(10,10), shadow=True, startangle=90, explode=explode)
plt.title('Physical abuse during pregnancy')
plt.xlabel('Locations across United States')
plt.ylabel('')