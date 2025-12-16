#Запитання 1.1. (1 бал). Скільки чоловіків і жінок присутні в цьому наборі даних? Значення ознаки genderне були вказані (чи «1» означає жінок, чи чоловіків) – з’ясуйте це, проаналізувавши зріст, зробивши припущення, що чоловіки в середньому вищі.

import pandas as pd
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

sns.set()
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker

sns.set_context(
    "notebook", font_scale=1.5, rc={"figure.figsize": (11, 8), "axes.titlesize": 18}
)

from matplotlib import rcParams

rcParams["figure.figsize"] = 11, 8

df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
print(df.head())

print(df.groupby('gender')['height'].agg(['mean', 'count']))
'''
1       161.355612  45530
2       169.947895  24470
'''
