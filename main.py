import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


# importing the dataset using the panda library
dataset = pd.read_csv("UberDataset.csv")

#---------------------------------------------
# print(dataset.head())
# print(dataset.tail())

#--------------------------------------------
# # shaping the dataset
# print(dataset.shape)

# --------------------------------------------
# # to understand the data more deeply : null values count, datatype, etc
# print(dataset.info())

# -----------------------------------------------
# ## data processing: replacing the null value with the NOT keyword
# print(dataset['PURPOSE'].fillna("NOT", inplace=True))

# ## changing start_date and end_date to the date_time format
# dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')
# dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

# ## changing the start_date to date and time 
# ## converting the time into four different categories i.e., Morning, Afternoon, Evening, Night


# dataset['date'] = pd

# -------------------------------------
# DATA VISUALISATION
# -------------------------------------
#1. In this, we will understand and compare all the columns in the dataset.

## Checking the unique values in the dataset of the columns:

obj = (dataset.dtypes == 'object')
object_columns = list(obj[obj].index)

unique_values = {}
for col in object_columns:
    unique_values[col] = dataset[col].unique().size
print(unique_values)