import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')

data['Age'] = pd.to_numeric(data['Age'], errors='coerce')

print(data.groupby('Sex')['Age'].mean())
''' Female    37.066593
Male      39.616483'''