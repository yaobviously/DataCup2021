# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:04:39 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import seaborn as sb

womens = pd.read_csv(r'https://raw.githubusercontent.com/bigdatacup/Big-Data-Cup-2021/main/hackathon_womens.csv')

womens.columns = womens.columns.str.lower().str.replace(' ', '_')

womens['gameid'] = womens['game_date'].astype(str) + womens['home_team'] + womens['away_team']

womncaa = womens[womens['home_team'].isin(['St. Lawrence Saints', 'Clarkson Golden Knights'])].reset_index()
womno = womens[~womens['home_team'].isin(['St. Lawrence Saints', 'Clarkson Golden Knights'])].reset_index()

womncaa

