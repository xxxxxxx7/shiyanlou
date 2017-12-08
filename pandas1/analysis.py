#!/usr/bin/env python3

import json
import pandas as pd


def analysis(file, user_id):
    times = 0
    minutes = 0
    try:
        df = pd.read_json(file)
    except ValueError:
    	return 0, 0



    df = df[df['user_id'] == user_id].minutes
    times = df.count()
    minutes = df.sum()
    return times, minutes

    
