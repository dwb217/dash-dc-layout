import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'WMATA'
myheading1 = 'Step Back! The doors are about to close! Ok, now...no wait, now.'
myheading2 = 'Better-ish'
image1 = 'rendering.png'
image2 = 'metro.png'
textbody = "Metro's recent on time performance has genuinely improved, but..."
sourceurl = 'https://www.wmata.com/about/back2good/index.cfm'
githublink = 'https://github.com/austinlasseter/dash-dc-layout'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading1),
    html.H2(myheading2),
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url(image1), style={'width': '50%', 'height': 'auto'})
        ],className='three columns'),
        html.Div([
            html.Img(src=app.get_asset_url(image2), style={'width': '80%', 'height': 'auto'}),
        ],className='three columns'),
        html.Div([
            html.Div(textbody, style={
                'padding': '40px',
                'font-size': '22px',
                'height': '240px',
                'border': 'thin red solid',
                'color': 'rgb(255, 255, 255)',
                'backgroundColor': 'rgb(57, 83, 107)',
                'textAlign': 'center',
                }),
        ],className='six columns'),
    ],className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
