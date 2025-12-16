import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')
print(data.info())
print(data['age'].unique())
# 1. Скільки чоловіків і жінок ( статева ознака) представлено в цьому наборі даних?
print(data['sex'].value_counts())
