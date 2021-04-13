import csv
import pandas as pd
import statistics
import plotly.figure_factory as pff
a=pd.read_csv('data.csv')
h=a['reading score'].to_list()
w=a['math score'].to_list()
ws=a['writing score'].to_list()

mean=sum(h)/len(h)
print(mean)
standardDeviation=statistics.stdev(h)
print(standardDeviation)
mode=statistics.mode(h)
print(mode)
median=statistics.median(h)
print(median)

mean=sum(w)/len(w)
print(mean)
standardDeviation=statistics.stdev(w)
print(standardDeviation)
mode=statistics.mode(w)
print(mode)
median=statistics.median(w)
print(median)

mean=sum(ws)/len(ws)
print(mean)
standardDeviation=statistics.stdev(ws)
print(standardDeviation)
mode=statistics.mode(ws)
print(mode)
median=statistics.median(ws)
print(median)

fig = pff.create_distplot([a["reading score"].tolist()], ["reading score"], show_hist=True)

fig.show()
