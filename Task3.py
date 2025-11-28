import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')
# 3. Який відсоток громадян Німеччини ( за ознакою рідної країни )?
print(data['Country'].unique())
print(data['Country'].value_counts(normalize=True))

'''
Country
Germany                       0.004311

'''