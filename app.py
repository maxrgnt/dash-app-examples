import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

########### Define your variables ######

myheading = "Population stats from 2000s"
mytitle = "by Spooky Creature"
x_values = list(range(2009,2019))
y1_values = [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]
y2_values = [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]
y3_values = [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]
y4_values = [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]
color1 = '#FF6B35'
color2 = '#FFD151'
color3 = '#136F63'
color4 = '#3E2F5B'
name1 = 'Pumpkins'
name2 = 'Cats'
name3 = 'Goblins'
name4 = 'Witches'
tabtitle = 'Spooky Sightings'
sourceurl = 'https://www.infoplease.com/us/population/us-population-state-1790-2015'
githublink = 'https://github.com/maxrgnt/dash-linechart-example'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode='lines+markers',
    marker = {'color': color1},
    line= dict(width=8, dash='dashdot'),
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode='lines+markers',
    marker = {'color': color2},
    line= dict(width=8, dash='dashdot'),
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode='lines+markers',
    marker = {'color': color3},
    line= dict(width=8, dash='dashdot'),
    name = name3
)
trace3 = go.Scatter(
    x = x_values,
    y = y4_values,
    mode='lines+markers',
    marker = {'color': color4},
    line= dict(width=8, dash='dashdot'),
    name = name4
)

# assign traces to data
data = [trace0, trace1, trace2, trace3]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
