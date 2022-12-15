# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 19:22:21 2022

@author: 2010330
"""


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
 
data = pd.read_csv("Skyserver.csv")
 
# converting column data to list
u = data['petroMag_u'].tolist()
g = data['petroMag_g'].tolist()
r = data['petroMag_r'].tolist()
i = data['petroMag_i'].tolist()
z = data['petroMag_z'].tolist()
err_u = data['petroMagErr_u'].tolist()
err_g = data['petroMagErr_g'].tolist()
err_r = data['petroMagErr_r'].tolist()
err_i = data['petroMagErr_i'].tolist()
err_z = data['petroMagErr_z'].tolist()

# graphing data
g_r = []
u_g = []

for item1, item2, item3 in zip(u, g, r):
    x = item2 - item3
    y = item1 - item2
    g_r.append(x)
    u_g.append(y)

l_x = np.linspace(5,-5,10000)
l_y = [-x + 2.22 for x in l_x]

plt.figure(1)
plt.scatter(g_r,u_g, marker = ".", color = "k")
plt.plot(l_x,l_y,color = "r")
plt.title('Color-Color Plot for 35 Suspected Abell 119 Members')
plt.xlabel('u - g')
plt.ylabel('g - r')
plt.xlim(0.5,1)
plt.ylim(0.5,2.5)
plt.savefig('color-color plot', dpi=300, orientation='portrait')
plt.show


plt.figure(2)
plt.scatter(g_r,u_g, marker = ".", color = "k")
plt.plot(l_x,l_y,color = "r")
plt.title('Color-Color Plot for 35 Suspected Abell 119 Members')
plt.xlabel('u - g')
plt.ylabel('g - r')
plt.xlim(-0.5,3)
plt.ylim(-0.5,2)
plt.savefig('color-color plot Strateva comp', dpi=300)
plt.show




# calculating percentages early and late
early = []
late = []

for itemaa, itembb in zip(g_r,u_g):
    if itemaa > -itembb + 2.22:
        early.append(itemaa)
    else:
        late.append(itemaa)

number_early = len(early)
number_late = len(late)
percentage_early = number_early/(number_early + number_late)
percentage_late = number_late/(number_early + number_late)
print("percentage early-type =", percentage_early,
      "percentage late-type =", percentage_late)
