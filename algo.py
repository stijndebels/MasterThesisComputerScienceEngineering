#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:59:51 2022

@author: stijndebels
"""
import ClosedPatternMiner
import pandas as pd 
from cpmpy import *

def myprint():
    print(Items.value())
    print(Trans.value())
    print("\n")
    
#implement closure constraint OK
#full table OK
#csv numpy OK
#make it more modular

nrT = 10
nrI = 5

 #store as csv file, read from it and use it, numpy.arrays

freq = 2
df = pd.read_csv('tdb.csv', index_col=0)
TDB = df.to_numpy()
print(TDB)
Items = boolvar(shape=nrI, name="items")
Trans = boolvar(shape=nrT, name="transactions")

    
closedPatternMiner = ClosedPatternMiner.ClosedPatternMiner(Trans, freq, nrI, nrT, TDB, Items)
closedPatternMiner.find_closed_patterns()
m = closedPatternMiner.get_model()
m+= (sum(Items[:]) >= 1)
m.solveAll(display=myprint)

 