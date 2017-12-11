# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:46:13 2017

@author: naren
"""
#Question : statewise distribution of women who came in hospital and stated that they smoked 3 months before pregnancy
import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('file_clean2.csv')
preg = preg.fillna('')

def format_text(preg):

    topic1= (preg.Break_Out == 'Smoker') & (preg.Response == 'YES') |  (preg.Response == 'YES (CHECKED)') 
    intersection = preg[topic1]

    #plot1 = intersection['Topic'].value_counts().unstack()
    plot1 = intersection.groupby('LocationDesc').Class.value_counts().unstack()
    
    plot2 = plot1.sort_values(by='Delivery', ascending= False)[:5]
    
    plot2.plot(kind='bar',colormap='winter', figsize=(16,6))
    
    plt.xlabel('Locations')
    plt.title('Statewise distribution of women who came in hospital and stated that they smoked 3 months before pregnancy')
    plt.show()

format_text(preg)