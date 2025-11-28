import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')
print(data.info())
print(data['Age'].unique())
# 1. Скільки чоловіків і жінок ( статева ознака) представлено в цьому наборі даних?
print(data['Sex'].value_counts())
''' Sex
Male      10860 
Female     5421'''