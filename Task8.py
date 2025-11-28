import numpy as np
import pandas as pd

data = pd.read_csv('adult_test.csv')

# 8. Серед кого більша частка тих, хто заробляє багато ( >50K): одружених чи самотніх чоловіків ( ознака сімейного стану )? Одруженими вважаються ті, чий сімейний стан починається з «Одружений» ( Married-civ-spouse, Married-spouse-absentабо Married-AF-spouse), решта вважаються неодруженими.
print(data['Martial_Status'].unique())
