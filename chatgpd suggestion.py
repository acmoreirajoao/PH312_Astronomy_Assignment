# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:22:55 2022

@author: Anaclare
"""

import pandas as pd
# import statsmodel.formula.api as smf
 
data = pd.read_csv("early.csv")
print(data)

# model = smf.ols('z ~ Early', data)
# print(model.params())