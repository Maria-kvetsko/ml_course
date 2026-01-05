#Обчисліть частки хворих людей (із серцево-судинними захворюваннями) у двох групах людей, описаних у завданні. Яке співвідношення цих двох часток?
import pandas as pd
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
print(df.info())
print(df['cholesterol'].unique())
df['age'] = round(df['age']/365.25).round().astype('int')
old_smoke_men = df[(df['gender']== 2) & (df['age']>= 60)& (df['age']<65)& (df['smoke']== 1)]
print(old_smoke_men)
probability_of_illness=old_smoke_men[(old_smoke_men['cholesterol']== 1)& (old_smoke_men['ap_hi']<120)]['cardio'].mean()
print(probability_of_illness)
the_probability_of_illness = old_smoke_men[(old_smoke_men['cholesterol']== 3)& (old_smoke_men['ap_hi']>=160)&(old_smoke_men['ap_hi']<180)]['cardio'].mean()
print(the_probability_of_illness)
print(the_probability_of_illness/probability_of_illness)
