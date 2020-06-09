#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 14:05:13 2020

@author: miriamcorona
"""

import pandas as pd
import glob
from glob import iglob
import os 
import numpy as np  

os.chdir('/Users/miriamcorona/Desktop/cap_proj')

# #this is the good code
path = '/Users/miriamcorona/Desktop/cap_proj'
allFiles = glob.glob(os.path.join(path,"*.csv"))

np_array_list = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    np_array_list.append(df.to_numpy())
    
comb_np_array = np.vstack(np_array_list)
big_frame = pd.DataFrame(comb_np_array)
big_frame.columns = ['Rating Period','State Fiscal Year', 'Model','County',
                      'Health Plan','Category of Aid','Lower Bound','Midpoint',
                      'Upper Bound']

big_frame.to_csv('output.csv')
# #this is the good code

#this put one column out of the scope
# path = '/Users/miriamcorona/Desktop/cap_proj/*.csv'

# all_rec = iglob(path, recursive=True)     
# dataframes = (pd.read_csv(f) for f in all_rec)
# big_dataframe = pd.concat(dataframes, ignore_index=True)
# all_files = glob.glob("*.csv")

# all_data = pd.DataFrame()
# for f in all_files:
#     df = pd.read_csv(f)
#     all_data = all_data.append(df,ignore_index=False)





