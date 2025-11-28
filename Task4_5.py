import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')
# 4-5. Які середнє значення та стандартне відхилення віку для тих, хто заробляє понад 50 тисяч на рік ( характеристика зарплати ), і тих, хто заробляє менше 50 тисяч на рік?
print(data[data['Target'] == ' <=50K.']['Age'].agg(['mean','std']))
print(data[data['Target']== ' >50K.']['Age'].agg(['mean','std']))

'''Більше 50к на рік
Name: proportion, dtype: float64
mean    38.710419
std     13.793616
Менше 50к на рік
Name: Age, dtype: float64
mean    39.528634
std     14.555459
'''