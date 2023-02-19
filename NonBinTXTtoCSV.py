import numpy
import pandas as pd
NAME = "soybean"

df = pd.read_csv(NAME+'.txt', sep=' ', header=None, comment='@')
TDBnonbinary = df.to_numpy()
TDB = numpy.zeros((630, 50))  # 0 is 630 1 is 50/17
for i in range(numpy.size(TDBnonbinary, 0)):
    for j in range(numpy.size(TDBnonbinary, 1) -1):
        TDB[i, TDBnonbinary[i][j]] = 1
df = pd.DataFrame(TDB)
df.to_csv(NAME+'.csv')