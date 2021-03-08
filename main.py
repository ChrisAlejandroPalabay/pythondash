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

app = dash.Dash('Philippines Covid-19 Tracker')

data_source = {"confirmed_cases": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv",
"deaths": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv",
"recovered": "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"}


def getContent(url):
  request = requests.get(url)
  content = request.content
  content = str(content,'utf-8')
  data = StringIO(content)
  df = pd.read_csv(data)
  return df

def unixTimeMillis(dt):
    return int(time.mktime(dt.timetuple()))

def unixToDate(unix):
    return datetime.datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d')

def getMarks(date):
    daterange = pd.date_range(start=date.min(), end=date.max(), freq='M')

    result = {}
    for i, date in enumerate(daterange):
        # Append value to dict
        result[unixTimeMillis(date)] = str(date.strftime('%Y-%m-%d'))

    return result

def getScatterFigure(x, y):
    return go.Figure([go.Scatter(x=x, y=y)])

def getCovidData(classification):
    data = getContent(data_source[classification])
    data = data[data['Country/Region']== 'Philippines']
    data = data.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])

    df = pd.DataFrame({'Date': data.columns, 'Case': data.values[0]})
    df['Date'] = df['Date'].apply(lambda x: str(x)[:-2] + '20' + str(x)[-2:])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Number of Case'] = df['Case'].diff()

    return df

############AC CODE
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
        res = "{} %↓, from the data gathered 30 days ago".format(ans)
        return res
    else:
        res = "{}%↑, from the data gathered 30 days ago".format(ans)
        return res

def newRecord(df):
    df = df.loc[df["Country/Region"] == "Philippines"]
    n2 = int(df.iloc[:,-1])
    n1 = int(df.iloc[:,-2])
    ans = str(n2 - n1)
    
    if "-" in ans:
        res = "None Recorded"
        return res
    else:
        return ans
    

def percent(a, b) : 
  
    result = float(((b - a) * 100) / a) 
  
    return result 

def getdate(df):
    d = str(df.columns[-1])
    res = "As of {}".format(d)
    return res

##########AC CODE
# Gather covid data
confirmed_cases = getCovidData('confirmed_cases')
deaths = getCovidData('deaths')
recovered = getCovidData('recovered')

dates = confirmed_cases['Date']

app.layout = html.Div(children=[
    html.H1(
        children='Philippines COVID-19 Tracker',
        style={
            'textAlign': 'center'
        }
    ),
    ##AC
    html.Div(children=[
    html.Div(className="maincon",children=[
        html.Div(className="con1",children=[
            html.Div(children=[
                html.H3("New COVID-19 Cases"),
                    html.Div(className="con2",children=[
                        html.P(newRecord(dfConfirmed)),
                    ]),
                html.P(getDifference(dfConfirmed))])
        ]),
    ]),

   html.Div(className="maincon",children=[
        html.Div(className="con1",children=[
            html.Div(children=[
                html.H3("New COVID-19 Deaths"),
                    html.Div(className="con2",children=[
                        html.P(newRecord(dfDeaths)),
                    ]),
                html.P(getDifference(dfDeaths))])
        ]),
    ]),
    html.Div(className="maincon",children=[
        html.Div(className="con1",children=[
            html.Div(children=[
                html.H3("New COVID-19 Recoveries"),
                    html.Div(className="con2",children=[
                        html.P(newRecord(dfRecovered)),
                    ]),
                html.P(getDifference(dfRecovered))])
        ]),
    ])
]),
#####AC


    html.Div(
        children=[
            html.Div(
                className="maincon",
                children=[
                    html.Div(
                    className='con1',
                    children=[
                        html.H3('Total Confirmed'),
                        html.P(
                            id='total_confirmed',
                            className='con2'
                        ),
                    ]
                ),
            ]),
            html.Div(
                className="maincon",
                children=[
                    html.Div(
                        className='con1',
                        children=[
                        html.H3('Total Deaths'),
                        html.P(
                            id='total_deaths',
                            className='con2'
                        )
                    ]
                ),
            ]),
            html.Div(
                className="maincon",
                children=[
                    html.Div(
                        className='con1',
                        children=[
                        html.H3('Total Recovered'),
                        html.P(
                            id='total_recovered',
                            className='con2'
                        )
                    ]
                ),
            ]),
        ],
        className='summary-container'
    ),

    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        id='active_cases_container',
                        style={
                            'background-color': 'black'
                        }
                    ),

                    html.Div(
                        id='deaths_container',
                        style={
                            'backgroundColor': 'black'
                        }
                    )
                ],
                style={
                    'display': 'flex'
                }
            )
        ],
        style={
            'color': 'black',
            'display': 'flex',
            'flexDirection': 'column',
            'alignItems': 'center'
        }
    ),

    dcc.RangeSlider(
                id='year_slider',
                min = unixTimeMillis(dates.min()),
                max = unixTimeMillis(dates.max()),
                value = [unixTimeMillis(dates.min()),
                         unixTimeMillis(dates.max())],
                marks=getMarks(dates)
    ),
    html.Div(id='placeholder')
]
)

@app.callback(
    Output('active_cases_container', 'children'),
    Output('deaths_container', 'children'),
    Output('total_confirmed', 'children'),
    Output('total_deaths', 'children'),
    Output('total_recovered', 'children'),
    Input('year_slider', 'value')
)

def update_fig(value):
    min = unixToDate(value[0])
    max = unixToDate(value[1])

    # Total number of case
    total_confirmed = confirmed_cases[confirmed_cases['Date'] == confirmed_cases['Date'].max()]
    total_confirmed = total_confirmed['Case']

    # Total number of deaths
    total_deaths = deaths[deaths['Date'] == deaths['Date'].max()]
    total_deaths = total_deaths['Case']

    # Total number of deaths
    total_recovered = recovered[recovered['Date'] == recovered['Date'].max()]
    total_recovered = total_recovered['Case']

    # Confirmed cases scatter figure
    df = confirmed_cases[(confirmed_cases['Date'] >= min) & (confirmed_cases['Date'] <= max)]
    fig = getScatterFigure(x=df['Date'], y=df['Number of Case'])
    confirmed_graph = dcc.Graph(
                        id='graph',
                        figure=fig,
                        className='graph'
                      )

    # Deaths scatter figure
    df = deaths[(deaths['Date'] >= min) & (deaths['Date'] <= max)]
    fig = getScatterFigure(x=df['Date'], y=df['Number of Case'])
    deaths_graph = dcc.Graph(
                        id='graph',
                        figure=fig
                      )

    # Recovered figure
    df = recovered[(recovered['Date'] >= min) & (recovered['Date'] <= max)]
    fig = getScatterFigure(x=df['Date'], y=df['Number of Case'])
    recovered_graph = dcc.Graph(
                        id='graph',
                        figure=fig
                      )

    return confirmed_graph, deaths_graph, total_confirmed, total_deaths, total_recovered



if __name__ == '__main__':
    app.run_server(port="8060")
