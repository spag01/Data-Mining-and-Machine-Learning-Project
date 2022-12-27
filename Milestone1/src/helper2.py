#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


# In[ ]:


#Helper Function -2 Used in Question 1.4 for imputing missing values

def impute_case(df):
  df['sex'].fillna("Missing", inplace=True)
  df['province'].fillna("Missing", inplace=True)
  df['country'].fillna("Missing", inplace=True)
  df['latitude'].fillna("Missing", inplace=True)
  df['longitude'].fillna("Missing", inplace=True)
  df['date_confirmation'].fillna("Missing", inplace=True)
  df['additional_information'].fillna("Missing", inplace=True)
  df['source'].fillna("Missing", inplace=True)
  df['chronic_disease_binary'].fillna("Missing", inplace=True)

  return df

