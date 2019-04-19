#!/usr/bin/python3
import os
import numpy as np
import pandas as pd

df1 = pd.read_csv(os.getcwd()+'/../out/pvp/batsmenMap')
columns=['batsmen','bowler','delivery','0s','1s','2s','3s','4s','5s','6s']
outFile = os.getcwd()+'/../out/pvp/batsmenRed'
f = open(outFile,'w')
f.write(",".join(columns)+"\n")
a = df1.groupby('batsmen')
batsmen = None
for key1, item1 in a:
    batsmen = str(key1)
    bowler = None
    delivery = None
    zero = None
    one = None
    two = None
    three = None
    four = None
    five = None
    six = None
    b = a.get_group(key1).groupby(['bowler'])
    for key2, item2 in b:
        bowler = str(key2)
        c = b.get_group(key2).groupby(['delivery'])
        for key3, item3 in c:
            delivery = str(key3)
            zero = str(c.get_group(key3)['0s'].sum())
            one = str(c.get_group(key3)['1s'].sum())
            two = str(c.get_group(key3)['2s'].sum())
            three = str(c.get_group(key3)['3s'].sum())
            four = str(c.get_group(key3)['4s'].sum())
            five = str(c.get_group(key3)['5s'].sum())
            six = str(c.get_group(key3)['6s'].sum())
            f.write(batsmen+","+bowler+","+delivery+","+zero+","+one+","+two+","+three+","+four+","+five+","+six+"\n")
f.close()

df2 = pd.read_csv(os.getcwd()+'/../out/pvp/bowlersMap')
columns=['batsmen','bowler','balls','wickets']
outFile = os.getcwd()+'/../out/pvp/bowlersRed'
f = open(outFile,'w')
f.write(",".join(columns)+"\n")
a = df2.groupby('batsmen')
batsmen = None
for key1, item1 in a:
    batsmen = str(key1)
    bowler = None
    balls = None
    wickets = None
    b = a.get_group(key1).groupby(['bowler'])
    for key2, item2 in b:
        bowler = str(key2)
        balls = str(b.get_group(key2)['balls'].sum())
        wickets = str(b.get_group(key2)['wickets'].sum())
        f.write(batsmen+","+bowler+","+balls+","+wickets+"\n")
f.close()

exit(1)