import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')

# 10. Підрахуйте середній час роботи ( годин на тиждень ) для тих, хто заробляє мало та багато ( зарплата ), для кожної країни ( країни походження ). Яким буде цей показник для Японії?
#hour_work = data[data['Hours_per_week']== ].mean()


#hour_work = (data.groupby(['Target', 'Country'])['Hours_per_week'].mean())
#print(hour_work)
print(pd.crosstab(index = data['native-country'], columns = data['salary'], values = data['hours-per-week'],aggfunc=np.mean))