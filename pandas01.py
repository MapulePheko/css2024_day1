# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:14:38 2024

@author: MAPULE PHEKO
"""

import pandas

file=pandas.read_csv("country_data.csv")

print(file)

print(file.info())

print(file.describe())

import pandas

file=pandas.read_csv("iris.csv")
print(file)
print(file.info())
print(file.describe())

import pandas
file=pandas.read_csv("insurance_data.csv",skiprows=5)
print(file)

print(file.info())

print(file.describe())
