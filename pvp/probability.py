#!/usr/bin/python3 
import os
import numpy as np
import pandas as pd

df = pd.read_csv(os.getcwd()+'/../out/pvp/aggregate')

df['0s'] = df['0s']/df['balls']
df['1s'] = df['1s']/df['balls']
df['2s'] = df['2s']/df['balls']
df['3s'] = df['3s']/df['balls']
df['4s'] = df['4s']/df['balls']
df['5s'] = df['5s']/df['balls']
df['6s'] = df['6s']/df['balls']

df['wickets'] = df['wickets']/df['balls']

df.to_csv(os.getcwd()+'/../out/pvp/probability',index=False,sep=',')

exit(1)