import pandas as pd
import csv
import plotly.graph_objects as go

#reading the file
df = pd.read_csv("data.csv")
#grouping the data by level and 
#calculating the mean for attempts in the level
print(df.groupby("level")["attempt"].mean())

#plotting a horizontal bar graph
fig = go.Figure(go.Bar(
            x = df.groupby("level")["attempt"].mean(),
            y = ['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation = 'h'))
fig.show()