import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importing the dataset using the panda library
dataset = pd.read_csv("UberDataset.csv")
dataset.head();

# shaping the dataset
dataset.shape

# to understand the data more deeply : null values count, datatype, etc
dataset.info();

## data processing: replacing the null value with the NOT keyword
dataset['PURPOSE'].fillna("NOT", inplace=True);

## changing start_date and end_date to the date_time format
dataset['START_DATE'] = pd.to_datetime(dataset['START_DATE'], errors='coerce')
dataset['END_DATE'] = pd.to_datetime(dataset['END_DATE'], errors='coerce')

## changing the start_date to date and time 
## converting the time into four different categories i.e., Morning, Afternoon, Evening, Night

from datetime import datetime

dataset['date'] = pd
