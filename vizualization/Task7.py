'''
Яка пара ознак має найсильнішу кореляцію Пірсона з ознакою статі ?

Кардіо, Холестерин

Висота, Куріння

Куріння, Алкоголь

Зріст, Вага
'''
import pandas as pd
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
import matplotlib.pyplot as plt
import seaborn as sns

corr_matrix = df.corr(method='pearson')

sns.heatmap(corr_matrix, annot=True)
plt.show()
