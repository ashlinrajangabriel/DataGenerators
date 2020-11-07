# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:52:03 2020

@author: z00403ff
"""

import numpy as np
import pandas as pd


import numpy as np 
import matplotlib.pyplot as plt 

import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)


# Using choice() method 
df = pd.DataFrame()
df["PID"] =  np.random.choice(11, 100000, p =[0.06006006,
0.03003003,
0.015015015,
0.12012012,
0.105105105,
0.045045045,
0.177177177,
0.039039039,
0.084084084,
0.135135135,
0.189189189
])
df['PID'].replace([0,1,2,3,4,5,6,7,8,9,10],['P1',
'P2',
'P3',
'P4',
'P5',
'P6',
'P7',
'P8',
'P9',
'P10',
'P11'],inplace=True)
  
count, bins, ignored = plt.hist(df["PID"], 14, density = True) 
plt.show()


item=[]
for items in df["PID"]:
    item_ = (random_date("2019-01-01", "2020-10-01", random.random() ))
    item.append(item_)
    
df["EntryDate"] =  item
df["SalesTaxPercent"] =  0.16
                  
df["VAT Percent"] =  0.19

df["GST Percent"] =  0.07

df["RangeCategory"] =  np.random.choice(12, 100000, p =[
0.07,
0.089,
0.085,
0.049,
0.042,
0.19,
0.14,
0.09,
0.07,
0.015,
0.09,
0.07

])
count, bins, ignored = plt.hist(df["RangeCategory"], 14, density = True) 
plt.show()
df['RangeCategory'].replace([0,1,2,3,4,5,6,7,8,9,10,11],[
'RC1',
'RC2',
'RC3',
'RC4',
'RC5',
'RC6',
'RC7',
'RC8',
'RC9',
'RC10',
'RC11',
'RC12'
],inplace=True)


df["CarrierID"] =  np.random.choice(3, 100000, p =[
0.3,
0.2,
0.5

])
count, bins, ignored = plt.hist(df["CarrierID"], 14, density = True) 
plt.show()

df['CarrierID'].replace([0,1,2,],[
'XC001',
'XC002',
'XC003'],inplace=True)



df["ItemDeclaredStatus"] =  np.random.choice(3, 100000, p =[0.5,
0.3,
0.2
])
df['ItemDeclaredStatus'].replace([0,1,2,],[
'Passed',
'Item misdeclared',
'Item not declared'],inplace=True)

df['DeclaredValueOfGood'] = ''
import scipy.stats as stats
for index , row in df.iterrows():
    if row['RangeCategory'] == 'RC1':
        upperLim = 0.5
        lowerLim = 50.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
   
    elif (row['RangeCategory'] ==  'RC2' ):
        upperLim = 50
        lowerLim = 250.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC3' ):
        upperLim = 250
        lowerLim = 300.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC4' ):
        upperLim = 300
        lowerLim = 500.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC5' ):
        upperLim = 500
        lowerLim = 900.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC6' ):
        upperLim = 900
        lowerLim = 1500.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC7' ):
        upperLim = 1500
        lowerLim = 3000.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC8' ):
        upperLim = 3000
        lowerLim = 5000.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC9' ):
        upperLim = 5001
        lowerLim = 9000.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC10' ):
        upperLim = 9001
        lowerLim = 10000.4
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC11' ):
        upperLim = 10001
        lowerLim = 30000
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)
    elif (row['RangeCategory'] ==  'RC12' ):
        upperLim = 31000
        lowerLim = 50000
        df.loc[index,"DeclaredValueOfGood"] = random.uniform(upperLim, lowerLim)


#Setting HAZARD FLAG
for index , row in df.iterrows():
    if (row['PID'] == 'P4' ):
       
        df.loc[index,"Flagged_Hazardous"] = 'X'

for index , row in df.iterrows():
    if (row['PID'] == 'P5' ):
       
        df.loc[index,"Flagged_Hazardous"] = 'X'


for index , row in df.iterrows():
    if (row['PID'] == 'P9' ):
       
        df.loc[index,"Flagged_Hazardous"] = 'X'


for index , row in df.iterrows():
    if (row['PID'] == 'P11' ):
       
        df.loc[index,"Flagged_Hazardous"] = 'X'


      
df['days_at_port'] = np.random.normal(9, 5, 100000)
df['Freight_Duration'] = (df['days_at_port'] - np.random.normal(2, 6, 100000)).round(0).astype(int)


import matplotlib.pyplot as plt
data = df
data.time = pd.to_datetime(data['EntryDate'], format='%Y-%m-%d')
plt.plot(data.EntryDate, data.DeclaredValueOfGood)



for index , row in df.iterrows():
    if (row['ItemDeclaredStatus'] == 'Item misdeclared' ):
       
        df.loc[index,"PenaltyIndicator"] = 'X'
        

for index , row in df.iterrows():
    if (row['ItemDeclaredStatus'] == 'PenaltyIndicator' ):
       
        df.loc[index,"PenaltyIndicator"] = 'X'
        
#Original value
