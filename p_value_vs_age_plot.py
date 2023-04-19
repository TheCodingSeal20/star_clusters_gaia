# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 17:13:12 2023

@author: rhbjo
"""

import json
import numpy as np
import matplotlib.pyplot as plt
import os

#%%
folder = 'C:/Users/rhbjo/OneDrive - The University of Nottingham/Shared/KS Test Data/'

file_list = os.listdir(folder)

pmr_p_values = np.zeros(len(file_list))
pmt_p_values = np.zeros(len(file_list))
cluster_ages = [1900, 331, 67.6, 225, 178, 278.6, 251.2, 72.6, 450, 135, 2570, 6600, 1800, 30.9, 1000, 120, 160, 1700]

for i in range(len(file_list)):
    data = json.load(open(folder + file_list[i]))
    pmr_p_values[i] = data['P Value']['pmr']
    pmt_p_values[i] = data['P Value']['pmt']
    
fig, ax = plt.subplots(2)

ax[0].scatter(cluster_ages, pmr_p_values)
ax[1].scatter(cluster_ages, pmt_p_values)
plt.show