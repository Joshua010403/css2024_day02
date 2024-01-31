# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:25:06 2024

@author: Joshua van Zyl
"""

""" 2. Extract, load, and Transform """


"""Extract Data"""


import pandas as pd

# Extract files from a different location

df = pd.read_csv("data02/country_data_index.csv")

# Extract files from a URL

#df = pd.read.csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

# Extract files from a URL and add headings

column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

df = pd.read_csv(url,header=None, names= column_names)


# Different file types

# Text files

df0 = pd.read_csv("data02/Geospatial Data.txt",sep=";")

# Excel files

df1 = pd.read_excel("data02/residentdoctors.xlsx")

# Json files

df2 = pd.read_json("data02/student_data.json")

url2 = "https://raw.githubusercontent.com/Asabele240701/css4_day02/main/effects-of-covid-19-on-trade-at-15-december-2021-provisional.csv"

df3 = pd.read_csv(url2)

print(df3.info())
print(df3.describe())

# df4 = pd.read.csv("chat_files/Accelerometer_data.csv", names = ["date_time", "x", "y", "z"])

# df = pd.read_jason("")

"""
Absolute Path

D:/OneDrive/NWU/2024/CSS/Week 1/Day Two/css2024_day2/data02/country_data_index.csv

Relative Path
data02/country_data_index.csv

"""


"""Transform Data"""


# Index Column

df = pd.read_csv("data02/country_data_index.csv",index_col=0)


# Skip Rows

df = pd.read_csv("data02/insurance_data.csv",skiprows=5)


# Inconsistent Data Types & Names

df = pd.read_excel("data02/residentdoctors.xlsx")

print(df.info())

df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')
df["UPPER_AGE"] = df["AGEDIST"].str.extract('-(\d+)')

print(df.info())

df["LOWER_AGE"] = df["LOWER_AGE"].astype(int)

print(df.info())


# Regular Expressions

"""
df["LOWER_AGE"] = df["AGEDIST"].str.extract('(\d+)-')

\d - refers to any digit 0-9
+ - can be multiple digits
- - followed by a hyphen
"""


"""
Working With dates

10-01-2024 - Everyone

01-10-2024 - USA

"""


df = pd.read_csv("data02/time_series_data.csv", index_col=0)

print(df.info())

df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")

print(df.info())

df['Year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Day'] = df['Date'].dt.day



"""NANS AND WRONG FORMATS"""

df = pd.read_csv("data02/patient_data_dates.csv")

# Allows you to see all rows
#pd.set_option('display.max_rows',None)

print(df)

"""
df.drop(["Index"],inplace=True,axis=1) # Drop index column


x = df["Calories"].mean() #Get mean of a column

df["Calories"].fillna(x, inplace = True) # Replace Nan cells with column mean


df["Date"] = pd.to_datetime(df["Date"], format="mixed") #Convert mixed date to date format

print(df)

df.dropna(subset=['Date'],inplace = True)           # Drops remaining NA rows
df = df.reset_index(drop = True)    # Fixes indexing for new rows

print(df)

df.drop_duplicates(inplace = True)  # Drops exact duplicate rows
df = df.reset_index(drop = True)    # Fixes indexing for new rows

print(df)

"""
# Drop Index Column:

df.drop(['Index'],inplace=True,axis=1)

print(df)

# Fill NaNs or empty fields in Calorie Column

x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

print(df)

# Convert Wrong Date Format in Date Column

df['Date'] = pd.to_datetime(df['Date'], format = "mixed")

# Drop NaT field in Date Column

df.dropna(subset=['Date'], inplace = True)

print(df)

df.loc[7, 'Duration'] = 45  # Fix incorrect data
#df['Duration'] = df['Duration'].replace([450],45)


# Remove any rows that have NaNs or empty fields
# Here only the row 1 for the MaxPulse column as the rest have been resolved
df.dropna(inplace = True)

# Reset index
df = df.reset_index(drop=True)

print(df)

# Remove duplicates found in line 10 and 11
df.drop_duplicates(inplace = True)

df = df.reset_index(drop=True)

print(df)



"""Applying Data Transformations"""


# Aggregation

df = pd.read_csv(url,header=None, names= column_names)

col_names = df.columns.tolist()

print(col_names)

df["sepal_length_sq"] = df["sepal_length"]**2 
df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2) # Better


grouped = df.groupby('class')

mean_square_values = grouped['sepal_length_sq'].mean()

sum_square_values = grouped['sepal_length_sq'].sum()

number_square_values = grouped['sepal_length_sq'].count()

print(mean_square_values)



# Append and Merge

df1 = pd.read_csv("data02/person_split1.csv")
df2 = pd.read_csv("data02/person_split2.csv")

df = pd.concat([df1,df2], ignore_index = True)
#df = df.reset_index(drop=True)


# Inner Join

df1 = pd.read_csv("data02/person_education.csv")
df2 = pd.read_csv("data02/person_work.csv")

df_merge_inner = pd.merge(df1,df2, on="id")

# Outer Join
df_merge_outer = pd.merge(df1,df2, on="id", how="outer")


df = pd.read_csv(url,header=None, names= column_names)
df['class'] = df['class'].str.replace("Iris-", "")


# Filtering

df = df[df['sepal_length'] > 5]
df = df[df['class'] == 'virginica']


# Load

df.to_csv("data02/output/iris_data_cleaned.csv")
df.to_csv("data02/output/iris_data_cleaned_no_index.csv", index = False)

df.to_excel("data02/output/iris_data_cleaned_no_index.xlsx", index = False, sheet_name = 'Sheet1')

df.to_json("data02/output/iris_data_cleaned.json", orient='records')
