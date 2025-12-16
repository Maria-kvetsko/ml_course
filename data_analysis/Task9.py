import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')

# 9. Яка максимальна кількість годин, яку людина працює на тиждень ( функція "години на тиждень" )? Скільки людей працюють таку кількість годин, і який відсоток >50Kсеред них тих, хто багато заробляє ( )?

print(data['salary'].unique())

data.info()

max_hours_per_week = data['hours-per-week'].max()
print(max_hours_per_week)
count_people_work_max_hours = (data['hours-per-week']== max_hours_per_week).sum()
print(count_people_work_max_hours)
subset = data[data['hours-per-week']== max_hours_per_week]
percent_rich = (subset['salary']=='>50K').mean()*100
print(percent_rich)

