#Створіть графік скрипки для зросту та статі, використовуючи violinplot(). Використовуйте параметри: hue розділити за статтю; scale оцінити кількість записів для кожної статі. Для коректного відображення графіка вам потрібно конвертувати його DataFrame у довгий формат за допомогою melt() функції from pandas.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')

df = pd.melt(df, value_vars=['height'], id_vars=['gender'])
sns.violinplot(x='variable', y='value', hue='gender',split= True, data=df, scale='count', scale_hue=False)
plt.show()
