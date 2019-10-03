import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np

########### Define your variables ######
myheading = "🎃 🧙 Spooky sightings over the years 👻 🧛"
list_of_options = [' Pumpkins ',' Witches ',' Ghosts ',' Vampires ']
list_of_images = ['pumpkin.jpg','witches.jpeg','ghost.png','vampire.jpeg']
colors = ['#FF6B35','#FFD151','#136F63','#3E2F5B']
locations = ['Castles','Graveyards','Haunted Houses','Forests']
tabtitle = 'spooktober'
sourceurl = 'https://www.timeanddate.com/countdown/halloween'
githublink = 'https://github.com/maxrgnt/pythdc2'

########### Set up the chart

def randomData(forYears):
    ''' Return an array of random data for the number of years passed in '''
    let numberOfYears = forYears
    # Create array of random number of sightings per year
    sightingsPerYear = np.random.randint(low=1, high=100, size=numberOfYears)
    # Multiplier to further randomize the number of sightings per year
    anotherRandomFactor = np.random.randint(low=1, high = 10, size = 1)[0]
    # Create array of new sightings per year
    newSightingsPerYear = [sightings*anotherRandomFactor for sightings in sightingsPerYear]
    # Return new array
    return newSightingsPerYear

def createTracesForData(forYears):
    ''' Create scatterplot instance for each location in the location array '''
    traces = []
    # Iterate over every item in location array to plot data for 
    for i in range(0,len(locations)):
        # Create range of years for x-axis
        yearRange = range(2019-forYears,2019)
        # Remove ',' from years (2,019 -> 2019)
        rangeOfYears =  [str(year).replace(',','') for year in yearRange]
        # Instance of scatter plot
        trace_i = go.Scatter(x = rangeOfYears
                             , y = randomData(forYears)
                             , name = locations[i]
                             , marker = {'color': colors[i]}
                             , mode = 'lines+markers'
                             , line = dict(width = 8, dash = 'dashdot')
                            )
        # Add instance to list of instances
        tracelist.append(trace_i)
    # Return array of scatterplots
    return tracelist

def createFigure(forYears):
    ''' Create sighting figure '''
    # Assign traces to data
    data = createTracesForData(forYears)
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
    html.H1(myheading),
        dcc.Slider(
            id='myslider',
            min=1,
            max=20,
            step=1,
            value=10,
            marks={
                1: '1 year',
                5: '5 years',
                10: '10 years',
                15: '15 years',
                20: '20 years'
            },
        ),
        html.Br(),
        html.H2('What sighting are you interested in?'),
        dcc.RadioItems(
            id='your_input_here',
            options=[
                    {'label':list_of_options[0], 'value':list_of_images[0]},
                    {'label':list_of_options[1], 'value':list_of_images[1]},
                    {'label':list_of_options[2], 'value':list_of_images[2]},
                    {'label':list_of_options[3], 'value':list_of_images[3]},
                    ],
            value=list_of_images[0],
            labelStyle={'display': 'inline-block'}
        ),
        html.Div(
            id='your_output_here', 
            children=''),
        dcc.Graph(
            id='figure-1',
            figure=createFigure(10)
        ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')])
def radio_results(radioButton):
    ''' Return picture for selected radio button '''
    return html.Img(src=app.get_asset_url(radioButton), style={'width': 'auto', 'height': '50%'})

@app.callback(Output('figure-1', 'figure'),
              [Input('your_input_here', 'value'),Input('myslider', 'value')])
def new_fig(radioButton,sliderVal):
    ''' Update graph with new random data when radio button or slider altered '''
    return createFigure(sliderVal)

############ Deploy
if __name__ == '__main__':
    app.run_server()
