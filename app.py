import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

########### Define your variables ######
# Important Links
sourceurl = 'https://www.timeanddate.com/countdown/halloween'
githublink = 'https://github.com/maxrgnt/pythdc2/blob/master/app.py'
# Content
tabtitle = 'spooktober'
myheading = "🎃 🧙 Spooky sightings over the years 👻 🧛"
# Static Data
locations = ['Castles','Graveyards','Haunted Houses','Forests']
locationColors = ['#FF6B35','#FFD151','#136F63','#3E2F5B']
objects = [' Pumpkins ',' Witches ',' Ghosts ',' Vampires ']
objectImages = ['pumpkin.jpg','witches.jpeg','ghost.png','vampire.jpeg']
# Dynamic Data
years = 10
yearRange = setYearRange(years)
sightingsByObjectByYear = generateRandomData(years)

def setYearRange(forYears):
    # Create range of years given # years passed in
    years = range(2019-forYears,2019)
    # Remove ',' from years (2,019 -> 2019)
    return [str(year).replace(',','') for year in years]

def generateRandomData(forYears):
    ''' Return an array of random data for the number of years passed in '''
    # Create array of random number of sightings per year
    z = []
    for x in range(0,len(objects)):
        xy = []
        for y in range(0,len(locations)):
            xy.append(list(np.random.randint(low=1, high=100, size=forYears)))
        z.append(xy)
    return z
    
########### Set up the chart

def createTraces(forObject,forYears):
    ''' Create scatterplot instance for each location in the location array '''
    traces = []
    # Iterate over every item in location array to plot data for
    for i in range(0,len(locations)):
        # Instance of scatter plot
        trace_i = go.Scatter(x = yearRange
                             , y = sightingsByObjectByYear[forObject][i]
                             , name = locations[i]
                             , marker = {'color': colors[i]}
                             , mode = 'lines+markers'
                             , line = dict(width = 8, dash = 'dashdot')
                            )
        # Add instance to list of instances
        traces.append(trace_i)
    # Return array of scatterplots
    return traces
    
def createFigure(forYears):
    ''' Create sighting figure '''
    # Assign traces to data
    data = createTraces(0,forYears)
    # Set layout
    layout = go.Layout()
    # Return figure
    return go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    # Heading
    html.H1(myheading),
    # Slider
    dcc.Slider(
        id='spookySliderInput',
        min=1, max=20,
        step=1, value=10,
        marks={1: '1 year', 5: '5 years', 10: '10 years', 15: '15 years', 20: '20 years'}
    ),
    # Break
    html.Br(),
    # Subheading
    html.H2('What sighting are you interested in?'),
    # Radio buttons
    dcc.RadioItems(
        id='spookyRadioInput',
        options=[
                {'label':list_of_options[0], 'value':[0,list_of_images[0]]},
                {'label':list_of_options[1], 'value':[1,list_of_images[1]]},
                {'label':list_of_options[2], 'value':[2,list_of_images[2]]},
                {'label':list_of_options[3], 'value':[3,list_of_images[3]]},
                ],
        value=[0,list_of_images[0]],
        labelStyle={'display': 'inline-block'}
    ),
    # Image output from radio buttons
    html.Div(
        id='spookyRadioOutput', 
        children=''),
    # Graph of data
    dcc.Graph(
        id='spookyGraphOutput',
#         figure = createFigure(10)
    ),
    # Various links
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback
@app.callback(Output('spookyRadioOutput', 'children'),
             [Input('spookyRadioInput', 'value')])
def updateImageUsing(radioInput):
    ''' Return picture for selected radio button '''
    return html.Img(src=app.get_asset_url(radioInput[1]), style={'width': 'auto', 'height': '50%'})

# @app.callback(Output('spookyGraphOutput', 'figure'),
#              [Input('spookyRadioInput', 'value'), Input('spookySliderInput', 'value')])
# def updateGraphUsing(radioInput,sliderInput):
#     ''' Update graph with new random data when radio button or slider altered '''
#     return createFigure(sliderInput)

############ Deploy
if __name__ == '__main__':
    app.run_server()
