# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:44:56 2024

@author: MAPULE PHEKO
"""
import pandas
file = pandas.read_csv("country_data.csv")
print(file)
age1=30
age2=25
age3=29

age=[30,25,29,46,22]
print(age)

print(age[0])

print(age[1])

print(min(age))

print(sum(age))

print(len(age))

average=sum(age)/len(age)

print(average)

g1="M"
g2="F"
g3="M"

gender= ["M","F","M"]

c1="South Africa"
c2="Lesotho"


#Dictionaries - key:value pairs
#cat: "a cute animal"

mammals ={"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}
print(mammals["cat"])

#Data frames

fruits=["apple","banana","orange","grape","kiwi"]

Size_nm=[9.8,10.1,13.2,8.7,20.5]

fruits_sizes={'fruits':fruits,'sizes':Size_nm}


#df=dataframe

import pandas as pd

df=pd.DataFrame(fruits_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].mean())

print(df.describe())

print(df[df['sizes']>10])

print(df[1:3])

prices=[10.00,12.50,16.00,23.00,7.00]

df['prices']=prices

df.drop(columns=['sizes'],inplace=True)

