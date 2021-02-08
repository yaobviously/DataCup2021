# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 12:38:30 2021

@author: yaobv
"""
import pandas as pd
import numpy as np
import seaborn as sb
import plotly.express as px
from plotly.offline import plot

# loading the dataframe and converting columns to lower case strings with _

ohl = pd.read_csv(r'https://raw.githubusercontent.com/bigdatacup/Big-Data-Cup-2021/main/hackathon_scouting.csv')
ohl.columns = ohl.columns.str.lower().str.replace(" ", "_")

# creating a game identifier. each game must be analysed separately because 
# game states matter

ohl['gameid'] = ohl['game_date'].astype(str) + ohl['home_team'] + ohl['away_team']

# creating a list of Erie Otters players since they'll be those with the most
# data available to analyse

ottersplayers = ohl[ohl['team'] == 'Erie Otters']['player'].unique()

# this simple function displays the shot events for each player. 
# i should take a few minutes to  enable it to accept 'event' as an argument

def playershots(x):
    player = ohl[(ohl['player'] == x) & ((ohl['event'] == 'Shot') | (ohl['event'] == 'Goal'))]
    return sb.kdeplot(x= 'x_coordinate', y='y_coordinate', data = player[ohl['event'] == 'Goal'], fill=False)

# creating dictionaries of games, players, and erie players for later

gamedict = dict.fromkeys(ohl['gameid'].unique())
playerdict = dict.fromkeys(ohl['player'].unique())
erieplayers = dict.fromkeys(ohl[ohl['team'] == 'Erie Otters']['player'].unique())

# adding man advantage and score differential columns to the dataframe 

ohl['5on5'] = ((ohl['home_team_skaters'] == 5) & (ohl['away_team_skaters'] == 5)).astype(int)
ohl['5on4home'] = ((ohl['home_team_skaters'] == 5) & (ohl['away_team_skaters'] == 4)).astype(int)
ohl['5on3home'] = ((ohl['home_team_skaters'] == 5) & (ohl['away_team_skaters'] == 3)).astype(int)
ohl['5on4away'] = ((ohl['away_team_skaters'] == 5) & (ohl['home_team_skaters'] == 4)).astype(int)
ohl['5on3away'] = ((ohl['away_team_skaters'] == 5) & (ohl['home_team_skaters'] == 3)).astype(int)
ohl['4on4'] = ((ohl['home_team_skaters'] ==4) & (ohl['away_team_skaters'] ==4)).astype(int)

ohl['tie'] = ((ohl['home_team_goals'] == ohl['away_team_goals'])).astype(int)
ohl['home_ahead_1'] = (ohl['home_team_goals'] - ohl['away_team_goals'] == 1).astype(int)
ohl['home_ahead_2'] = (ohl['home_team_goals'] - ohl['away_team_goals'] == 2).astype(int)
ohl['home_ahead_3ormore'] = (ohl['home_team_goals'] - ohl['away_team_goals'] >= 3).astype(int)

ohl['away_ahead_1'] = (ohl['away_team_goals'] - ohl['home_team_goals'] == 1).astype(int)
ohl['away_ahead_2'] = (ohl['away_team_goals'] - ohl['home_team_goals'] == 2).astype(int)
ohl['away_ahead_3ormore'] = (ohl['away_team_goals'] - ohl['home_team_goals'] >=3).astype(int)

ohl.loc[ohl['home_ahead_1']][['home_team_goals', 'away_team_goals', 'home_ahead_1', 'home_ahead_2']]

# adding shot and goal 'tags' and computing the rolling average of shots/goals.
# estimating how events/event sequences change exp shots and goals seems 
# potentially important. maybe first thing to target?

ohl['is_shot'] = (ohl['event'] == 'Shot').astype(int)
ohl['is_goal'] = (ohl['event'] == 'Goal').astype(int)
ohl['shots_next_ten'] = ohl['is_shot'][::-1].rolling(10).sum()
ohl['goal_next_ten'] = ohl['is_goal'][::-1].rolling(10).sum()

ohl['possSet'] = (ohl['team'] != ohl['team'].shift(1)).cumsum()


# creating a (very low quality!) animated plot using Plotly to display events 
# over time.  initially the x,y coordinates are plotted as the index 
# increments, but animation_frame = 'clock' is what it should be (i think)

ohlg0 = ohl.loc[ohl['gameid'] == '2019-09-20Erie OttersSudbury Wolves']
ohlg0s = ohlg0.iloc[0:200,]


fig = px.scatter(ohlg0s,
                 x="x_coordinate",
                 y="y_coordinate",
                 animation_frame= ohlg0s.index,
                 animation_group="event",
                 hover_name="event",
                 range_x=[0,200],
                 range_y=[0,85])

plot(fig)
