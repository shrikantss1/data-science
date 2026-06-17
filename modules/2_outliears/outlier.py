import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataset = pd.DataFrame([[1000], [2000], [3000], [100000000], [4000], [5000], [6000], [7000], [8000]], columns=['salary'])

print("Data set:")
print(dataset.describe())

print(f"\n\nMean: \n{dataset.mean()}")


sns.distplot(dataset['salary'])
plt.show()


def outlier_detector(columns):
    sorted(columns)
    Q1, Q3 = np.percentile(columns, [25,75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)

    return (lower_range, upper_range)

lr, ur = outlier_detector(dataset['salary'])

print(f"Lower Range: {lr} Upper Range: {ur}")

print("Removing outliers")

pricessedData = dataset[(dataset['salary'] >= lr) & (dataset['salary'] <= ur)]


sns.distplot(pricessedData['salary'])

plt.show()

