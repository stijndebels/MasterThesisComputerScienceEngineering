#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Wed Dec 14 12:59:51 2022

@author: stijndebels
"""
from _ast import Global

import numpy

import ClosedPatternMiner
import pandas as pd
from cpmpy import *

x = 0

def counter():
    global x
    x +=1

# implement closure constraint OK
# full table OK
# csv numpy OK
# make it more modular

nrT = 630
nrI = 50
# store as csv file, read from it and use it, numpy.arrays

freq = 63
# df = pd.read_csv('tdb.csv', index_col=0)

df = pd.read_csv('soybean.csv', index_col=0)
TDB = df.to_numpy()
# input("Press Enter to continue...")

Items = boolvar(shape=nrI, name="items")
Trans = boolvar(shape=nrT, name="transactions")

closedPatternMiner = ClosedPatternMiner.ClosedPatternMiner(Trans, freq, nrI, nrT, TDB, Items)
closedPatternMiner.find_frequent_patterns()
m = closedPatternMiner.get_model()
m += (sum(Items[:]) >= 1)
m.solveAll(display=counter)
print("standard: "+str(x))

x=0
closedPatternMiner.find_closed_patterns()
m.solveAll(display=counter)
m = closedPatternMiner.get_model()
print("closed: "+str(x))
