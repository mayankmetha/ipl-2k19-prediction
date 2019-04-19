#!/usr/bin/python3
import os
import numpy as np
import pandas as pd

dfBat = pd.read_csv(os.getcwd()+'/../out/clustering/bat',sep = ':', header = None, names = ['batsmen','batCluster'])
dfBowl = pd.read_csv(os.getcwd()+'/../out/clustering/bowl',sep = ':', header = None, names = ['bowler','bowlCluster'])

df1 = pd.read_csv(os.getcwd()+'/../datasets/kaggle/runsSplit18.csv')
df1['batsmen'] = df1['batsmen'].map(dfBat.set_index('batsmen')['batCluster'])
df1['bowler'] = df1['bowler'].map(dfBowl.set_index('bowler')['bowlCluster'])
df1.dropna(axis=0,inplace=True)
df1.batsmen = df1.batsmen.astype('int32')
df1.bowler = df1.bowler.astype('int32')
df1.to_csv(os.getcwd()+'/../out/pvp/batsmenMap',sep=",",index=False)

df2 = pd.read_csv(os.getcwd()+'/../datasets/kaggle/ballSplit18.csv')
df2['batsmen'] = df2['batsmen'].map(dfBat.set_index('batsmen')['batCluster'])
df2['bowler'] = df2['bowler'].map(dfBowl.set_index('bowler')['bowlCluster'])
df2.dropna(axis=0,inplace=True)
df2.batsmen = df2.batsmen.astype('int32')
df2.bowler = df2.bowler.astype('int32')
df2.to_csv(os.getcwd()+'/../out/pvp/bowlersMap',sep=",",index=False)

exit(1)