import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading = "Population stats from 2000s"
mytitle = "by Spooky Creature"
x_values = list(range(2009,2019))
list_of_options = ['Pumpkins','Witches']
list_of_images = ['pumpkin.jpg','witch.jpg']
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

# def populate():
#     return list(np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10))

########### Set up the chart
def randList():
    return [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]

def createTraces():
    # create traces
    trace0 = go.Scatter(
        x = x_values,
        y = randList(),
        mode='lines+markers',
        marker = {'color': color1},
        line= dict(width=8, dash='dashdot'),
        name = name1
    )
    trace1 = go.Scatter(
        x = x_values,
        y = randList(),
        mode='lines+markers',
        marker = {'color': color2},
        line= dict(width=8, dash='dashdot'),
        name = name2
    )
    trace2 = go.Scatter(
        x = x_values,
        y = randList(),
        mode='lines+markers',
        marker = {'color': color3},
        line= dict(width=8, dash='dashdot'),
        name = name3
    )
    trace3 = go.Scatter(
        x = x_values,
        y = randList(),
        mode='lines+markers',
        marker = {'color': color4},
        line= dict(width=8, dash='dashdot'),
        name = name4
    )
    return[trace0,trace1,trace2,trace3]

# assign traces to data
data = createTraces()
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
        dcc.RadioItems(
        id='your_input_here',
        options=[
                {'label':list_of_options[0], 'value':list_of_images[0]},
                {'label':list_of_options[1], 'value':list_of_images[1]},
                ],
        value=list_of_images[0],
        labelStyle={'display': 'inline-block'}
        ),
    html.Div(id='your_output_here', children=''),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'}),

############ Deploy
if __name__ == '__main__':
    app.run_server()
