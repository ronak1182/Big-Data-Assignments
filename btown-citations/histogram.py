from __future__ import division, print_function
import numpy as np
import pandas as pd
import pygal as pygal
data = pd.read_csv('2016-first-quarter-citations.csv')
data = data.dropna(how='any')

from datetime import datetime
data['DateTime Issued'] = data.apply(lambda row: datetime.strptime(row['Date Issued'] + ':' + row['Time Issued'], '%m/%d/%y:%I:%M %p'), axis=1)

ages = data['Cited Person Age']
ages = ages[ages < 100]

list = [0]*100
for x in ages:
    list[int(x)] += 1

hist = pygal.Histogram()
q1_age = []

for i in range(0,len(list)):
    q1_age.append((list[i], i, i+1))

hist.add('ages',q1_age)
hist.render_to_file('q1_age.svg')
