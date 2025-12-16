import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')

# 7. Відобразіть статистику віку для кожної раси ( ознака раси ) та кожної статі ( ознака статі ). Використовуйте groupby() та describe() . Знайдіть максимальний вік чоловіків відповідної Amer-Indian-Eskimoраси.
print(data['race'].unique())
print(data.groupby(['sex', 'race'])['age'].describe())
