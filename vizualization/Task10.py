#Який найменший вік, у якому кількість людей із серцево-судинними захворюваннями (ССЗ) перевищує кількість людей без ССЗ?

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
df['age'] = round(df['age']/365.25).round().astype('int')
sns.countplot(x='age', hue='cardio', data=df)
plt.show()