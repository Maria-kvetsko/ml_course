import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')


# 6. Чи правда, що люди, які заробляють понад 50 тисяч доларів, мають щонайменше середню освіту? ( освіта – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters або Doctorate функція)
print(pd.crosstab(data['salary'],data['education']))
