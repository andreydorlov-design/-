import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Андрей\Downloads\flights_NY.csv')

df_clean = df.dropna(subset=['air_time', 'distance'])

df_clean = df_clean[df_clean['air_time'] > 0]

df_clean['speed'] = (df_clean['distance'] / df_clean['air_time']) * 60

df_wn_ua = df_clean[df_clean['carrier'].isin(['WN', 'UA'])].copy()

df_wn_ua.to_csv('flights_speed_WN_UA_clean.csv', index=False)
