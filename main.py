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
    index2 = 30
    df = df.loc[dfConfirmed["Country/Region"] == "Philippines"]
    n2 = int(df.iloc[:,-index1])
    n1 = int(df.iloc[:,-index2])
    ans = str(float("{:.2f}".format(percent(n1,n2)))) 

    if "-" in ans:
        res = "Decreased by {}%".format(ans)
        return res
    else:
        res = "Increased by {}%".format(ans)
        return res


def percent(a, b) : 
  
    result = float(((b - a) * 100) / a) 
  
    return result 

app = dash.Dash()
app.layout = html.Div([

    html.Div(children=[
        html.Div([
                html.H2("Diff Confirmed Cases"),
                html.P(getDifference(dfConfirmed))
        ])
    ],style={
        'border-style': 'solid'
     }
    ),

    html.Div(children=[
        html.Div([
                html.H2("Diff deaths"),
                html.P(getDifference(dfDeaths))
        ])
    ],style={
        'border-style': 'solid'
     }
    )
        
])

if __name__ == "__main__" : 
    app.run_server(debug=True)