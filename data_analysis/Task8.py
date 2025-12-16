import numpy as np
import pandas as pd

data = pd.read_csv('adult_data.csv')

# очищаємо пробіли і прибираємо NaN
for col in ['marital-status', 'sex', 'salary']:
    data[col] = data[col].astype(str).str.strip()

data = data.dropna(subset=['marital-status', 'sex', 'salary'])

marital_status = ["Married-civ-spouse", "Married-spouse-absent", "Married-AF-spouse"]

# фільтр
married = data[(data['marital-status'].isin(marital_status)) & (data['sex'] == 'male')]
single = data[(~data['marital-status'].isin(marital_status)) & (data['sex'] == 'male')]

# перевіримо, чи є дані
print("Одружених чоловіків:", len(married))
print("Неодружених чоловіків:", len(single))

# доля тих, хто заробляє більше
married_share = (married['salary'] == '>50K').sum() / len(married) if len(married) > 0 else 0
single_share = (single['salary'] == '>50K').sum() / len(single) if len(single) > 0 else 0

print("Частка одружених чоловіків з доходом >50K:", married_share)
print("Частка неодружених чоловіків з доходом >50K:", single_share)
