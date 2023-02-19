#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:12:02 2023

@author: stijndebels
"""
from cpmpy import *
from PatternMiner import PatternMiner

class ClosedPatternMiner(PatternMiner):
    def __init__(self,Trans,freq,nrI,nrT,TDB,Items):
        super().__init__(Trans,freq,nrI,nrT,TDB,Items)
       # self.m = Model()
    def find_closed_patterns(self):
        #self.find_frequent_patterns()
        for i in range (self.nrI):
            som2 = 0
            for t in range(self.nrT):
                som2 +=(1-self.TDB[t][i])*self.Trans[t]
            self.m += (self.Items[i] == (som2==0))
    
