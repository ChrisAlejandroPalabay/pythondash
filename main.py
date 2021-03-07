import requests
import time
import dash
import datetime
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output
from io import StringIO

confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovery = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"

dfConfirmed = pd.read_csv(confirmed)
dfDeaths = pd.read_csv(deaths)
dfRecovered = pd.read_csv(recovery)

def getDifference(df) :
    
    index1 = 1
    index2 = 20
    df = df.loc[df["Country/Region"] == "Philippines"]
    n2 = int(df.iloc[:,-index1])
    n1 = int(df.iloc[:,-index2])
    ans = str(float("{:.2f}".format(percent(n1,n2)))) 

    if "-" in ans:
        res = "Decreased by {} %, from the data gathered 30 days ago".format(ans)
        return res
    else:
        res = "Increased by {}%, from the data gathered 30 days ago".format(ans)
        return res


def percent(a, b) : 
  
    result = float(((b - a) * 100) / a) 
  
    return result 

app = dash.Dash()
app.layout = html.Div(children=[

    html.Div(children=[
        html.Div([
            html.Div([
                html.H2("COVID-19 Cases"),
                html.P(getDifference(dfConfirmed))
            ])
        ],style={
                'text-align': 'center',
                'background-color': '#7E3EEF',
                'font-family': 'Verdana',
                'color': 'white'
        })
    ],style={
        'width': '340px',
        'height':  '120px',
        'border-style': 'solid',
        'background-color': '#7E3EEF',
        'display':'inline-block',
        'margin-right': '17px',
        'margin-left': '17px'
    }
    ),
    html.Div(children=[
        html.Div([
            html.Div([
                html.H2("COVID-19 Deaths"),
                html.P(getDifference(dfDeaths))
            ])
        ],style={
                'text-align': 'center',
                'background-color': '#7E3EEF',
                'font-family': 'Verdana',
                'color': 'white'
        })
    ],style={
        'width': '340px',
        'height':  '120px',
        'border-style': 'solid',
        'background-color': '#7E3EEF',
        'display':'inline-block',
        'margin-right': '17px',
        'margin-left': '17px'
    }
    ),
    html.Div(children=[
        html.Div([
            html.Div([
                html.H2("COVID-19 Recoveries"),
                html.P(getDifference(dfRecovered))
            ])
        ],style={
                'text-align': 'center',
                'background-color': '#7E3EEF',
                'font-family': 'Verdana',
                'color': 'white'
        })
    ],style={
        'width': '340px',
        'height':  '120px',
        'border-style': 'solid',
        'background-color': '#7E3EEF',
        'display':'inline-block',
        'margin-right': '17px',
        'margin-left': '17px'
    }
    )    
],style={
    
})

if __name__ == "__main__" : 
    app.run_server(debug=True)