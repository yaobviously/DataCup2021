# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:38:30 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import seaborn as sb

ohl = pd.read_csv(r'https://raw.githubusercontent.com/bigdatacup/Big-Data-Cup-2021/main/hackathon_scouting.csv')
ohl.columns = ohl.columns.str.lower().str.replace(" ", "_")

ohl['gameid'] = erie['game_date'].astype(str) + erie['home_team'] + erie['away_team']

ottersplayers = ohl[ohl['team'] == 'Erie Otters']['player'].unique()

def playershots(x):
    player = erie[(erie['Player'] == x) & ((erie['Event'] == 'Shot') | (erie['Event'] == 'Goal'))]
    return sb.displot(x= 'X Coordinate', y='Y Coordinate', data = player[player['Event'] == 'Goal'], kind='kde')

