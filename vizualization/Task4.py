#Яка заокруглена різниця між медіанними значеннями віку (у місяцях) для некурців та курців? Вам потрібно буде визначити одиниці вимірювання ознаки age в цьому наборі даних.
import pandas as pd
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
print(df.info())
df['age'] = df['age']/365.25
mean_age = df.groupby(['smoke'])['age'].median()
print(round((mean_age[0]*12)-(mean_age[1]*12)))