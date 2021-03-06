import pandas as pd

confirmed = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
deaths = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
recovery = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"



def percent(a, b) : 
  
    result = int(((b - a) * 100) / a) 
  
    return result 
  
if __name__ == "__main__" : 
  
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    
    res = percent(a,b)
    print(res, "%") 
              