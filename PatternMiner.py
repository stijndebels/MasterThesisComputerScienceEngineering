#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 11:58:24 2023

@author: stijndebels
"""
from cpmpy import *

class PatternMiner:
    def __init__(self,Trans,freq,nrI,nrT,TDB,Items):
        self.Trans=Trans
        self.freq=freq
        self.nrI = nrI
        self.nrT = nrT
        self.TDB = TDB
        self.Items=Items
        self.m = Model()
    def find_covered_patterns(self):
        for t in range(self.nrT):
            som = 0
            for i in range(self.nrI):
                som +=(1-self.TDB[t][i])*self.Items[i]
            self.m += (self.Trans[t] == (som<= 0))
    def find_frequent_patterns(self):
        self.find_covered_patterns()
        self.m += (sum(self.Trans[:]) >= self.freq)
    def get_model(self):
        return self.m;
        