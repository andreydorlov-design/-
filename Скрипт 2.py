import pandas as pd
import numpy as np

df = pd.read_csv(r'C:\Users\Андрей\Downloads\flights_NY.csv')

mean_air_time_per_plane = df.groupby('tailnum')['air_time'].mean().reset_index()
mean_air_time_per_plane.columns = ['tailnum', 'mean_air_time_minutes']

mean_air_time_per_plane = mean_air_time_per_plane.dropna()

mean_air_time_per_plane.to_csv('mean_air_time_per_plane.csv', index=False)

mu = mean_air_time_per_plane['mean_air_time_minutes'].mean()
sigma = mean_air_time_per_plane['mean_air_time_minutes'].std()

params_df = pd.DataFrame({'parameter': ['mean', 'std'], 'value': [mu, sigma]})
params_df.to_csv('normal_params.csv', index=False)

print("Успех")
