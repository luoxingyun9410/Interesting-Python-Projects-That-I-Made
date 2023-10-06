import requests as req
import pandas as pd
import json

res = req.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo")
data = json. loads(res. text)
df = pd. DataFrame(data)
df.to_csv(r'C:/Users/steven.luo/Documents/Python project/Interesting-Python-Projects-That-I-Made/stock live update/test 1.csv')