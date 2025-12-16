import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')

data['age'] = pd.to_numeric(data['age'], errors='coerce')

print(data.groupby('sex')['age'].mean())
