import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')
# 4-5. Які середнє значення та стандартне відхилення віку для тих, хто заробляє понад 50 тисяч на рік ( характеристика зарплати ), і тих, хто заробляє менше 50 тисяч на рік?
print(data[data['salary'] == '<=50K']['age'].agg(['mean','std']))
print(data[data['salary']== '>50K']['age'].agg(['mean','std']))

