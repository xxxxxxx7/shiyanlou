#!/usr/bin/env python3

import json
import pandas as pd
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

file = '/home/shiyanlou/Code/user_study.json'
df = pd.read_json(file)


data = df.groupby('user_id').sum()

fig = plt.figure()

ax = fig.add_subplot(1,1,1) 

ax.set_title('StudyData')

ax.set_xlabel("User ID")
ax.set_ylabel("Study Time")

ax.plot(data.index, data.minutes)

plt.show()