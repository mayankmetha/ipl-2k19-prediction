#!/usr/bin/python3 
import os
import numpy as np
import pandas as pd

df1 = pd.read_csv(os.getcwd()+'/../out/pvp/batsmenRed')
df1['0s'] = df1['0s']/df1['balls']
df1['1s'] = df1['1s']/df1['balls']
df1['2s'] = df1['2s']/df1['balls']
df1['3s'] = df1['3s']/df1['balls']
df1['4s'] = df1['4s']/df1['balls']
df1['5s'] = df1['5s']/df1['balls']
df1['6s'] = df1['6s']/df1['balls']
df1.to_csv(os.getcwd()+'/../out/pvp/runsProb',index=False,sep=',')

df2 = pd.read_csv(os.getcwd()+'/../out/pvp/bowlersRed')
df2['wickets'] = df2['wickets']/df1['balls']
df2.to_csv(os.getcwd()+'/../out/pvp/wicketsProb',index=False,sep=',')

exit(1)