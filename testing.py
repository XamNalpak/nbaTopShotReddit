import pandas as pd

from datetime import datetime


data = pd.read_csv('nbatop.csv')

print(len(data))

print(data.drop_duplicates(subset=['url'],keep='last').count())

print(len(data))
