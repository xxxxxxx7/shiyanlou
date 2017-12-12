#!/usr/bin/env python

# -*- coding:-8 -*-

import pandas as pd
from pandas import Series, DataFrame



def quarter_volume():

    data = pd.read_csv('/home/shiyanlou/Code/apple.csv',header=0)

    df = data.Volume
    df.index = pd.to_datetime(data.Date)
    second_volume = df.resample('Q').sum().sort_values()[-2]
    return second_volume



