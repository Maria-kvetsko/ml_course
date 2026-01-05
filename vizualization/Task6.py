'''
Медіанний ІМТ у вибірці знаходиться в межах нормальних значень.

ІМТ у жінок в середньому вищий, ніж у чоловіків.

У здорових людей середній ІМТ вищий, ніж у хворих.

У сегменті здорових та непитущих чоловіків ІМТ ближчий до норми, ніж у сегменті здорових та непитущих жінок
'''
import pandas as pd
df = pd.read_csv('vizualization/mlbootcamp5_train.csv')
df.info()
print(df['height'])
df['imt']= df['weight']/(df['height']/100)**2
print(df['imt'])
df.info()
print(df['imt'].median())

print(df.groupby('gender')['imt'].mean())

print(df.groupby('cardio')['imt'].mean())

print(df.groupby(['gender', 'alco', 'cardio'])['imt'].median())