#Яка заокруглена різниця між відсотками курців серед чоловіків і жінок?
import pandas as pd
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
print(df.info())
sum_smoke= df.groupby('gender')['smoke'].mean()
print(round(100*(df.loc[df['gender']== 2, 'smoke'].mean()- df.loc[df['gender']== 1, 'smoke'].mean())))

'''
20
'''
