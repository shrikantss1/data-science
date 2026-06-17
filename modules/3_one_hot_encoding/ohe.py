import pandas as pd
import numpy as np

data = pd.read_csv('../../data/preprocessExample.csv')

print(data.info())

data['Country'] = data['Country'].fillna(data['Country'].mode()[0])
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())

print(data.info())


#OneHotEncoding

df1 = pd.get_dummies(data['Country'], dtype=int)
df2 = data.iloc[:, [1,2,3]]

final_dataset = pd.concat([df1, df2], axis = 1)

print(final_dataset.info())

print(final_dataset)