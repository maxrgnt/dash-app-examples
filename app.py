import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

from dash.dependencies import Input, Output, State

########### Define your variables ######

myheading = "Spooky creature sightings 👻"
x_values = list(range(2009,2019))
list_of_options = ['Pumpkins','Witches']
list_of_images = ['pumpkin.jpg','witch.jpg']
colors = ['#FF6B35','#FFD151','#136F63','#3E2F5B']
places = ['Castles','Graveyards','Haunted Houses','Forests']
tabtitle = 'spooktober'
sourceurl = 'https://www.timeanddate.com/countdown/halloween'
githublink = 'https://github.com/maxrgnt/pythdc2'

########### Set up the chart
def randList():
    return [np.random.randint(low=1, high = 10, size = 1)[0]*n for n in np.random.randint(low=1, high=100, size=10)]

def createTraces():
    tracelist = []
    for i in range(0,len(colors)):
        trace_i = go.Scatter(x = x_values, y = randList()
                             , mode = 'lines+markers'
                             , marker = {'color': colors[i]}
                             , line = dict(width = 8, dash = 'dashdot')
                             , name = places[i]
                            )
        tracelist.append(trace_i)
    return tracelist

def create_fig():
    # assign traces to data
    data = createTraces()
    layout = go.Layout()
    return go.Figure(data=data,layout=layout)

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
        figure=create_fig()
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

########## Define Callback
@app.callback(Output('your_output_here', 'children'),
              [Input('your_input_here', 'value')]
             )
def radio_results(image_you_chose):
    return html.Img(src=app.get_asset_url(image_you_chose), style={'width': 'auto', 'height': '50%'})

@app.callback(Output('figure-1', 'figure'),
              [Input('your_input_here', 'value')]
             )
def new_fig():
    return create_fig()

############ Deploy
if __name__ == '__main__':
    app.run_server()
