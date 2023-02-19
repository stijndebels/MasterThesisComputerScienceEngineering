#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:50:06 2023

@author: stijndebels
"""

import pandas as pd 


TDB = [ [0, 1, 0, 0 ,0], 
        [0, 0, 0, 0 ,1], 
        [1, 0, 1, 0, 0], 
        [1, 0, 0, 0, 1], 
        [0, 1, 1, 0 ,0],
        [0, 0, 0, 1 ,1],
        [0, 0, 1, 1 ,1],
        [1, 1, 1, 0 ,0],
        [1, 1, 0, 0 ,1],
        [1, 1, 1, 0 ,1],
    
    ] #store as csv file, read from it and use it, numpy.arrays

df = pd.DataFrame(TDB)
df.to_csv('tdb.csv')