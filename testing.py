import pandas as pd

from datetime import datetime


data = pd.read_csv('nbatop.csv')



newDF = data[data['date'] >= datetime.now().strftime('%Y-%m-%d')]

