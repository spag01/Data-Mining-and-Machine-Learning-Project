#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math


# In[ ]:


#Helper Function -1 Used in Question 1.4 for changing age brackets to integer (Eg. 20-25, 80-)

from ctypes import resize
def map_fn(age: str):
  if '-' in age:
    res = age.split('-')
    if res[0] and res[1]:
      n1, n2 = res[0], res[1]
      if n1 and n2:
        ret = math.ceil((int(n1)+int(n2)) // 2)
        return ret
    else:
        return res[0]
  else:
    return age

