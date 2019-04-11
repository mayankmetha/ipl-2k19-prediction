#!/usr/bin/python3

import os
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

bat = pd.read_csv(os.getcwd()+'/../datasets/PlayerStatsIPL/bat.csv')
batC = pd.DataFrame()
batC['Ave'] = bat['Ave']
batC['SR'] = bat['SR']
batC['Mat'] = bat['Mat']
batC.replace('-',0,inplace=True)
kmeans = KMeans(n_clusters=7).fit(batC)

out = os.getcwd()+'/../out/clustering/bat.csv'
exp = pd.DataFrame(bat.values[:, 1])
exp['Cluster'] = kmeans.labels_
exp.to_csv(out,index=False,sep=':',header=False)

bowl = pd.read_csv(os.getcwd()+'/../datasets/PlayerStatsIPL/bowl.csv')
bowlC = pd.DataFrame()
bowlC['Ave'] = bowl['Ave']
bowlC['Econ'] = bowl['Econ']
bowlC['SR'] = bowl['SR']
bowlC.replace('-',0,inplace=True)
kmeans = KMeans(n_clusters=7).fit(bowlC)

out = os.getcwd()+'/../out/clustering/bowl.csv'
exp = pd.DataFrame(bowl.values[:, 1])
exp['Cluster'] = kmeans.labels_
exp.to_csv(out,index=False,sep=':',header=False)