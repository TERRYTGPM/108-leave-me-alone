import plotly.express
import plotly.figure_factory as ff
import pandas

df = pandas.read_csv("e.csv")

AvgRating = df["AvgRating"]

fig = ff.create_distplot([AvgRating], ["Sr.No,Mobile Brand"])
fig.show()