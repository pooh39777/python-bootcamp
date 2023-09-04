import pandas as pd

pd.DataFrame()
pd.pivot_table()

#create dataframe

raw_data = {
  "name": ["Ant", "Bird", "Cat", "Dog"],
  "age": [9, 10, 15, 20],
  "gender": ["F", "M", "F", "M"]
}

df = pd.DataFrame(raw_data)
df

#create new column
df['city'] = 'London'

df.shape #see df dimension

#remove column
df = df.drop('city', axis = 1) #axis = 0 for index/row, axis = 1 for column
df

#remove index
df = df.drop(2, axis = 0)
df

#reset index (because index no.2 was removed)
df = df.reset_index(drop = True)
df

#column names
list(df.columns)

#rename columns
df.columns = ['nickname', 'age', 'sex']
df

#Series vs DataFrame
type(df['nickname'])
type(df)

#create a new series
s1 = pd.Series(['Mary', 20, 'F'], index = ['nickname', 'age', 'sex'])
print(s1)
type(s1)

#append s1 to df
df = df._append(s1, ignore_index=True)
df

s2 = pd.Series(['London', 'Paris', 'Bangkok', 'Phitsanulok'])
df['city'] = s2
df

#write csv file
df.to_csv('mydata.csv')

#import csv file
df2 = pd.read_csv('mydata.csv')
df2

#import excel file
df3 = pd.read_excel('data.xlsx')
df3

#import json
df4 = pd.read_json('data.json')
df4

#check data type of column
df4['amazonRating'].dtype
