# -*- coding: utf-8 -*-
"""
Created on Sun Dec 03 14:30:42 2017

@author: naren
"""

import pandas as pd
import matplotlib.pyplot as plt

preg=pd.read_csv('CDC_PRAMStat_Data_for_2011.csv')
preg = preg.fillna('')

preg['Question'].replace('(*PCH) During the 12 months before you got pregnant did your husband or partner push  hit  slap, kick, choke, or physically hurt you in any other way?','(*PCH) During the 12 months before you got pregnant, did your husband or partner push, hit, slap, kick, choke, or physically hurt you in any other way?', inplace=True)

print(preg.head())
#preg.to_csv("file_clean.csv",index=False)