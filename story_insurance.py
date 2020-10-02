# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 22:23:36 2020

@author: Queenie
"""
#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns

df = pd.read_csv("insurance.csv")

#sescribing the df
print(df.shape)

df = df.dropna()
print(df.shape)


#standardizing variables
df = df.replace({"man":"male"})
df = df.replace({'woman':'female'})
pd.options.display.max_rows
df = df.replace({'n.east':'northeast'})
df = df.replace({'n.west':'northwest'})
df = df.replace({'s.east':'southeast'})
df = df.replace({'s.west':'southwest'})

#creating a new column for BMI stats - defines whether a person is underweight...
rating = [
    (df['bmi']< 18.5),
    (df['bmi']>= 18.5) & (df['bmi'] < 24.9),
    (df['bmi']>= 24.9) & (df['bmi'] < 29.9),
    (df['bmi']>= 29.9),
    ]

label = ['underweight','normal','overweight','obese']
df['bmi_stats'] = np.select(rating,label)


#printing the tables
print(df[['sex', 'children']].groupby(['sex']).agg(["mean","max", "min"]))
print(df[['sex', 'bmi']].groupby(['sex']).agg(["mean", "max", "min"]))
print(df[['sex', 'charges']].groupby(['sex']).agg(["mean", "max", "min"]))
print(df[['children', 'charges']].groupby(['children']).agg(["mean", "max", "min"]))
#print(df[['region', 'charges']].groupby(['region']).agg(["mean", "max", "min"]))
print(df[['bmi', 'charges']].groupby(['bmi']).agg(["mean", "max", "min"]).sort_values('bmi', ascending=True))
print(df[['bmi_stats', 'charges']].groupby(['bmi_stats']).agg(["mean", "max", "min"]))
#print("\n")
print(df[['sex', 'bmi_stats']].groupby(['sex',"bmi_stats"]).size())

#seaborn charts
sns.boxplot('children','charges',data=df)
sns.set_style("dark")
plt.title("Charges paid according to number of children")

sns.relplot('bmi_stats','charges',data=df, hue='sex')
sns.relplot('bmi','charges',data=df, hue='sex')
plt.title("Charges paid according to BMI")
sns.pairplot(data=df, hue='sex')

sns.set_style("whitegrid")
#sns.set_style("dark")

#mathplotlib charts
plotdata = pd.DataFrame({
    "male":[8,104,186,375],
    "female":[12,116,190,344],
    
    
    }, 
    index=["underweight","normal","overweight","obese"]
)

plotdata.plot(kind="bar")
plt.title("BMI Stats per gender")


bardata = pd.DataFrame({
    "female":[12569.59],
    "male":[13963.95]
    },
    index = ["charges"]
)

bardata.plot(kind="bar")
plt.title("Average charges being paid per gender")

#if interested to create a new csv, just uncomment
#df.to_csv('modified_insurance2.csv',index=False)

