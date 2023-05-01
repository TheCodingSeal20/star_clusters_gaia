# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 17:41:04 2023

@author: rhbjo
"""

#%%Functions

from data_handler import *
from anisotropy_parameter import *
import numpy as np
import matplotlib.pyplot as plt
import copy

plt.rcParams.update({'font.size': 15}) 

#%%Files and Folders

cluster = 'NGC 5460'

data_folder = 'C:/Users/rhbjo/OneDrive - The University of Nottingham/Shared/Final Data/'
data = Data(data_folder + f'{cluster}-final.json')

plot_folder = 'C:/Users/rhbjo/OneDrive - The University of Nottingham/Shared/Updated Figures/AP radial dependence/'

save = False

#%%Producing graphs

anisotropy_parameter(data, plot=True)
if save == True:
    plt.savefig(plot_folder + f'{cluster}-ap_plot.png', dpi=1000)