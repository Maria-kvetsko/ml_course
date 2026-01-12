'''
Обчисліть та побудуйте матрицю кореляції, використовуючи коефіцієнт рангової кореляції Спірмена .
Яка пара ознак має найсильнішу рангову кореляцію Спірмена?
Зріст, Вага
Вік, Вага
Холестерин, Глюк
Кардіо, Холестерин
Ап_хі, Ап_ло
Куріння, Алкоголь
Чому ці ознаки мають сильну рангову кореляцію?
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
corr = df[['height','weight','age','cholesterol','gluc','cardio','ap_hi','ap_lo','smoke', 'alco']].corr(method='spearman')
sns.heatmap(corr,annot=True, fmt='.1f' )
plt.show()
