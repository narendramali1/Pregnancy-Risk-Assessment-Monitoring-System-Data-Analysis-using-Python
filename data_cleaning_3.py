# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 17:31:48 2017

@author: naren
"""

import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('CDC_PRAMStat_Data_for_2011.csv')
preg = preg.fillna('')

preg['Geolocation_X']= preg.Geolocation_X + "," + preg.Geolocation_Y

del preg['Geolocation_Y']
preg.to_csv("file_clean2.csv",index=False)