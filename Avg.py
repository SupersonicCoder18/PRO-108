import pandas as pd
import plotly.express as ps
import plotly.figure_factory as ff

df = pd.read_csv("Rate.csv")
Avg = df["Avg Rating"].tolist()

fig = ff.create_distplot([Avg], ["Average Rating"])
fig.show()