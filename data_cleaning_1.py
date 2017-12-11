# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:17:36 2017

@author: naren
"""

import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('CDC_PRAMStat_Data_for_2011.csv')
preg.dropna()

new_label= ['Year', 'LocationAbbreviation', 'LocationDescription', 'Class', 'Topic',	
            'Question', 'DataSource', 'Response', 'Data_Value_Unit', 'Data_Value_Type', 
            'Data_Value', 'Data_Value_Footnote_Symbol', 'Data_Value_Footnote', 'Data_Value_Std_Error', 
            'Low_Confidence_Limit', 'High_Confidence_Limit', 'Sample_Size', 'Break_Out', 
            'Break_Out_Category', 'Geolocation_X', 'Geolocation_Y', 'ClassID', 'TopicID', 'QuestionID',
            'LocationID', 'BreakOutID', 'BreakOutCategoryID', 'ResponseID']
df=pd.read_csv('CDC_PRAMStat_Data_for_2011.csv', header=0,names= new_label)
print(df.head())