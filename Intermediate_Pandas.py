import pandas as pd

penguins = pd.read_csv("penguins.csv")

#preview first and last 5 rows
penguins.head()
penguins.tail()

#shape of dataframe
penguins.shape

#info of dataframe
penguins.info()

#select column
penguins['species']
penguins.species
penguins.species.head()
penguins.species.head(8)
penguins[['species', 'island', 'sex']].head()

#integer location based indexing (iloc)
penguins.iloc[0]
penguins.iloc[[0, 1, 2]]
penguins.iloc[0:3] #upto 3, but not including 3 (silmilar to 0, 1, 2)
penguins.iloc[0:5, [0, 1, 5]]

#filter rows by a condition
penguins[ penguins['island'] == 'Torgersen' ]
penguins[ penguins['bill_length_mm'] < 34 ]

#filter more than one condition
penguins[ (penguins['island'] == 'Torgersen') & (penguins['bill_length_mm'] < 35) ]
filter_penguins = penguins[ (penguins['island'] == 'Torgersen') | (penguins['bill_length_mm'] < 35) ]

#filter with .query()
penguins.query('island == "Torgersen" & bill_length_mm < 35') #or "island == 'Torgersen'"

#check missing
penguins.isna()
penguins.isna().sum()

#filter missing values
penguins['sex'].isna()

#drop na
clean_penguins = penguins.dropna()
clean_penguins.head(10)

#fill missing values
avg_value = penguins['bill_length_mm'].mean()
print(avg_value)

fill_penguins = penguins['bill_length_mm'].fillna(value = avg_value)
fill_penguins

#sort low to high, high to low
penguins.sort_values('bill_length_mm')
penguins.sort_values('bill_length_mm', ascending = False).head(10)

#sort multiple columns
penguins.dropna().sort_values(['island', 'bill_length_mm'])

#unique values
penguins['species'].unique()

#count values
penguins['species'].value_counts()

#count more than one columns
result = penguins[['island', 'species']].value_counts() #multi-index
result = penguins[['island', 'species']].value_counts().reset_index()

result.columns = ['island', 'species', 'count']
result

#summarise dataframe
penguins.describe()
penguins.describe(include = 'all') #include non-numeric column

#avg, sd
penguins['bill_length_mm'].mean()
penguins['bill_length_mm'].std()
penguins['bill_length_mm'].median()

#group by
# penguins[penguins['species'] == 'Adelie']['bill_length_mm'].mean()
penguins.groupby('species')['bill_length_mm'].sum()

#group by & aggregation
penguins.groupby('species')['bill_length_mm'].agg(['min', 'max', 'mean'])
penguins.groupby(['island', 'species'])['bill_length_mm'].agg(['min', 'max', 'mean'])

#use \ help to read code to the next line
result2 = penguins.groupby(['island', 'species'])['bill_length_mm']\
  .agg(['min', 'max']).reset_index()

#write to csv
result2.to_csv('result2.csv')

#map values MALE: m, FEMALE: f (input as dictionary)
penguins['sex'].head()
penguins['sex_new'] = penguins['sex'].map({'MALE': 'm', 'FEMALE': 'f'}).fillna('other')
penguins.head()

#numpy
import numpy as np
np.mean(penguins['bill_length_mm'])

#other functions of numpy
np.sum(penguins['bill_length_mm'])
np.std(penguins['bill_length_mm'])

#where
score = pd.Series([80, 90, 76, 63, 10])
grade = np.where(score >= 80, "passed", "failed")
print(grade)

df = penguins.query("species == 'Adelie' ")[['species', 'island', 'bill_length_mm']].dropna()
df.head()

df['new_column'] = np.where(df['bill_length_mm'] > 40, True, False)
df.head(10)

#merge
#result = pd.merge(left_df, right_df, on="key_column")

#histogaram one column
penguins['body_mass_g'].plot(kind = 'hist')

import matplotlib.pyplot as plt
plt.show() #to show plot

plt.clf() #to clear previous plot
penguins['bill_length_mm'].plot(kind = 'hist', bins = 30, color = "black")
plt.show()

#histogram two columns
plt.clf()
penguins[['body_mass_g', 'bill_length_mm']].plot(kind = 'hist')
plt.show()

#bar plot for species
plt.clf()
penguins['species'].value_counts().plot(kind = 'bar', color = ['salmon', 'orange', 'gold'])
plt.show()

#scatter plot
plt.clf()
penguins[['bill_length_mm', 'bill_depth_mm']]\
  .plot(x='bill_length_mm', y='bill_depth_mm', kind="scatter")
plt.show()
