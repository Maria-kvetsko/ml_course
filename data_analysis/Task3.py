import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')
# 3. Який відсоток громадян Німеччини ( за ознакою рідної країни )?
print(data['native-country'].unique())
print(data['native-country'].value_counts(normalize=True))
