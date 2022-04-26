# Importing Modules
import pandas as pd
import plotly.express as px

# Initializing Data
df = pd.read_csv("data.csv")

# Printing Some Text
print()
print("-----------------------Corona Cases Worldwide Using Graphs-----------------------")
print("Ploting At Your Browser..")
print()

# Data In Scatter Chart
fig = px.scatter(df, x="date", y="cases", color="country", size="cases", size_max=15, title="Corona Cases Worldwide(Scatter Chart)")
fig.show()
print("Corona Cases Worldwide(Scatter Chart)")
print()

# A Bar Graph Or A Line Graph Could Be A Better Option. So,
# Bar Chart
figBar = px.bar(df, x="date", y="cases", color="country", title="Corona Cases Worldwide(Bar Chart)")
figBar.show()
print("Corona Cases Worldwide(Bar Chart)")
print()

# Line Chart
figLine = px.line(df, x="date", y="cases", color="country", title="Corona Cases Worldwide(Line Chart)")
figLine.show()
print("Corona Cases Worldwide(Line Chart)")
print()

"""***So, This is how the data of Corona Cases can be displayed in different types of graphs/charts.***"""
