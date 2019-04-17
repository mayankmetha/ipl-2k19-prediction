#!/usr/bin/python3
import os
import numpy as np
import pandas as pd

df1 = pd.read_csv(os.getcwd()+'/../out/pvp/dataset')
columns=['batsmen','bowler','0s','1s','2s','3s','4s','5s','6s','balls','wickets']
outFile = os.getcwd()+'/../out/pvp/aggregate'
f = open(outFile,'w')
f.write(",".join(columns)+"\n")

a = df1.groupby('batsmen')
batsmen = None
for key1, item1 in a:
    batsmen = str(key1)
    bowler = None
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    balls = None
    wickets = None
    b = a.get_group(key1).groupby(['bowler'])
    for key2, item2 in b:
        bowler = str(key2)
        zero = str(b.get_group(key2)['0s'].sum())
        one = str(b.get_group(key2)['1s'].sum())
        two = str(b.get_group(key2)['2s'].sum())
        three = str(b.get_group(key2)['3s'].sum())
        four = str(b.get_group(key2)['4s'].sum())
        five = str(b.get_group(key2)['5s'].sum())
        six = str(b.get_group(key2)['6s'].sum())
        balls = str(b.get_group(key2)['balls'].sum())
        wickets = str(b.get_group(key2)['wickets'].sum())
        f.write(batsmen+","+bowler+","+zero+","+one+","+two+","+three+","+four+","+five+","+six+","+balls+","+wickets+"\n")

f.close()
exit(1)