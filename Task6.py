import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')


# 6. Чи правда, що люди, які заробляють понад 50 тисяч доларів, мають щонайменше середню освіту? ( освіта – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters або Doctorate функція)
print(pd.crosstab(data['Target'],data['Education']))
'''
Education  10th  11th  12th  1st-4th  5th-6th  7th-8th  9th  Assoc-acdm  Assoc-voc  Bachelors  Doctorate  HS-grad  Masters  Preschool  Prof-school  Some-college
Target                                                                                                                                                          
<=50K.      431   605   209       77      165      287  228         386        518       1578         56     4455      434         31           64          2911
>50K.        25    32    15        2       11       22   14         148        161       1092        125      828      500          1          194           676
'''
