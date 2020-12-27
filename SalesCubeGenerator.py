# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:57:57 2020

@author: Asus
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




df["Products"] =  np.random.choice(12, 100000, p =[0.09,0.089,0.085,0.049,0.042,0.19,0.14,0.09,0.07,0.015,0.09,0.05])

item=[]
for items in df["Products"]:
    item_ = (random_date("2019-01-01", "2020-12-01", random.random() ))
    item.append(item_)
    
df["OrderDate"] =  item


df['Products'].replace([0,1,2,3,4,5,6,7,8,9,10,11],['SA80','AK-47','MG34','Lewis','M3','Beretta AR70','Colt','Remington 870',
'M19','AR15','RPG','UZI'],inplace=True)


for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        df.loc[index,"ProductsDescription"] = "Assault Rifle"
   
    elif (row['Products'] ==  'AK-47' ):
        df.loc[index,"ProductsDescription"] = "Automatic Rifle"
    elif (row['Products'] ==  'MG34' ):
        df.loc[index,"ProductsDescription"] = "General-purpose machine gun"
    elif (row['Products'] ==  'Lewis' ):
        df.loc[index,"ProductsDescription"] = "Light machine gun"
    elif (row['Products'] ==  'M3' ):
        df.loc[index,"ProductsDescription"] = "submachine gun"
    elif (row['Products'] ==  'Beretta AR70' ):
        df.loc[index,"ProductsDescription"] = "Assault rifle"
    elif (row['Products'] ==  'Colt' ):
        df.loc[index,"ProductsDescription"] = "Revolver"
    elif (row['Products'] ==  'Remington 870' ):
        df.loc[index,"ProductsDescription"] = "Shotgun"
    elif (row['Products'] ==  'M19' ):
        df.loc[index,"ProductsDescription"] = "Revolver"
    elif (row['Products'] ==  'AR15' ):
        df.loc[index,"ProductsDescription"] = "Self-loading rifle"
    elif (row['Products'] ==  'RPG' ):
        df.loc[index,"ProductsDescription"] = "shoulder-fired missile"
    elif (row['Products'] ==  'UZI' ):
        df.loc[index,"ProductsDescription"] = "Submachine gun"

for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        df.loc[index,"ProductCategory"] = "Rifle"
   
    elif (row['Products'] ==  'AK-47' ):
        df.loc[index,"ProductCategory"] = "Rifle"
    elif (row['Products'] ==  'MG34' ):
        df.loc[index,"ProductCategory"] = "Machine gun"
    elif (row['Products'] ==  'Lewis' ):
        df.loc[index,"ProductCategory"] = "Machine gun"
    elif (row['Products'] ==  'M3' ):
        df.loc[index,"ProductCategory"] = "Submachine gun"
    elif (row['Products'] ==  'Beretta AR70' ):
        df.loc[index,"ProductCategory"] = "Rifle"
    elif (row['Products'] ==  'Colt' ):
        df.loc[index,"ProductCategory"] = "Revolver"
    elif (row['Products'] ==  'Remington 870' ):
        df.loc[index,"ProductCategory"] = "Shotgun"
    elif (row['Products'] ==  'M19' ):
        df.loc[index,"ProductCategory"] = "Revolver"
    elif (row['Products'] ==  'AR15' ):
        df.loc[index,"ProductCategory"] = "Rifle"
    elif (row['Products'] ==  'RPG' ):
        df.loc[index,"ProductCategory"] = "Missile"
    elif (row['Products'] ==  'UZI' ):
        df.loc[index,"ProductCategory"] = "Submachine gun"

df['ManufacturedCountry'] = ''

for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        df.loc[index,"ManufacturedCountry"] = "United Kingdom"
   
    elif (row['Products'] ==  'AK-47' ):
        df.loc[index,"ManufacturedCountry"] = "Russia"
    elif (row['Products'] ==  'MG34' ):
        df.loc[index,"ManufacturedCountry"] = "Germany"
    elif (row['Products'] ==  'Lewis' ):
        df.loc[index,"ManufacturedCountry"] = "United Kingdom"
    elif (row['Products'] ==  'M3' ):
        df.loc[index,"ManufacturedCountry"] = "United States"
    elif (row['Products'] ==  'Beretta AR70' ):
        df.loc[index,"ManufacturedCountry"] = "Italy"
    elif (row['Products'] ==  'Colt' ):
        df.loc[index,"ManufacturedCountry"] = "United States"
    elif (row['Products'] ==  'Remington 870' ):
        df.loc[index,"ManufacturedCountry"] = "United States"
    elif (row['Products'] ==  'M19' ):
        df.loc[index,"ManufacturedCountry"] = "Italy"
    elif (row['Products'] ==  'AR15' ):
        df.loc[index,"ManufacturedCountry"] = "United States"
    elif (row['Products'] ==  'RPG' ):
        df.loc[index,"ManufacturedCountry"] = "Russia"
    elif (row['Products'] ==  'UZI' ):
        df.loc[index,"ManufacturedCountry"] = "Israel"

for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        df.loc[index,"ProductCost"] = "500"
   
    elif (row['Products'] ==  'AK-47' ):
        df.loc[index,"ProductCost"] = "1800"
    elif (row['Products'] ==  'MG34' ):
        df.loc[index,"ProductCost"] = "350"
    elif (row['Products'] ==  'Lewis' ):
        df.loc[index,"ProductCost"] = "200"
    elif (row['Products'] ==  'M3' ):
        df.loc[index,"ProductCost"] = "2500"
    elif (row['Products'] ==  'Beretta AR70' ):
        df.loc[index,"ProductCost"] = "2750"
    elif (row['Products'] ==  'Colt' ):
        df.loc[index,"ProductCost"] = "251"
    elif (row['Products'] ==  'Remington 870' ):
        df.loc[index,"ProductCost"] = "300"
    elif (row['Products'] ==  'M19' ):
        df.loc[index,"ProductCost"] = "275"
    elif (row['Products'] ==  'AR15' ):
        df.loc[index,"ProductCost"] = "1950"
    elif (row['Products'] ==  'RPG' ):
        df.loc[index,"ProductCost"] = "3000"
    elif (row['Products'] ==  'UZI' ):
        df.loc[index,"ProductCost"] = "2300"

df["CustomerID"] =  np.random.choice(11, 100000, p =[0.06006006,0.03003003,0.015015015,0.12012012,0.105105105,0.045045045,
0.177177177,0.039039039,0.084084084,0.135135135,0.189189189])

for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        upperLim = -20
        lowerLim = 150
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
   
    elif (row['Products'] ==  'AK-47' ):
        upperLim = 30
        lowerLim = 250
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'MG34' ):
        upperLim = 15
        lowerLim = 90
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'Lewis' ):
        upperLim = -5
        lowerLim = 100
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'M3' ):
        upperLim = -15
        lowerLim = 90
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'Beretta AR70' ):
        upperLim = -39
        lowerLim = 90
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'Colt' ):
        upperLim = -15
        lowerLim = 60
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'Remington 870' ):
        upperLim = -45
        lowerLim = 275
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'M19' ):
        upperLim = 25
        lowerLim = 125
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'AR15' ):
        upperLim = 20
        lowerLim = 150
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'RPG' ):
        upperLim = -120
        lowerLim = 150
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)
    elif (row['Products'] ==  'UZI' ):
        upperLim = -40
        lowerLim = 110
        df.loc[index,"SalePricePerPiece"] = int(df["ProductCost"][index]) + random.uniform(upperLim, lowerLim)

df.sort_values(by=['OrderDate'], inplace=True)

for index , row in df.iterrows():
    if row['Products'] == 'SA80':
        upperLim = 6
        lowerLim = 200
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
   
    elif (row['Products'] ==  'AK-47' ):
        upperLim = 6
        lowerLim = 250
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'MG34' ):
        upperLim = 15
        lowerLim = 90
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'Lewis' ):
        upperLim = 20
        lowerLim = 100
        df.loc[index,"QuantityPurchased"] =  round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'M3' ):
        upperLim = 25
        lowerLim = 100
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'Beretta AR70' ):
        upperLim = 1
        lowerLim = 200
        df.loc[index,"QuantityPurchased"] =  round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'Colt' ):
        upperLim = 1
        lowerLim = 200
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'Remington 870' ):
        upperLim = 5
        lowerLim = 50
        df.loc[index,"QuantityPurchased"] = round( random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'M19' ):
        upperLim = 15
        lowerLim = 100
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'AR15' ):
        upperLim = 25
        lowerLim = 150
        df.loc[index,"QuantityPurchased"] =  round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'RPG' ):
        upperLim = 2
        lowerLim = 15
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))
    elif (row['Products'] ==  'UZI' ):
        upperLim = 20
        lowerLim = 200
        df.loc[index,"QuantityPurchased"] = round(random.uniform(upperLim, lowerLim))


df['Currency']= 'USD'
df['CustomerID'].replace([0,1,2,3,4,5,6,7,8,9,10],['CUST01','CUST02','CUST03','CUST04','CUST05','CUST06','CUST07','CUST08','CUST09','CUST010','CUST011'],inplace=True)
df["CustomerCity"] =  np.random.choice(7, 100000, p =[0.03,0.04,0.02,0.1,0.2,0.4,0.21])
df['CustomerCity'].replace([0,1,2,3,4,5,6],['Kandy','Chennai','Colombo','Lagos','Bangalore','Frankfurt','Mumbai'],inplace=True)
for index , row in df.iterrows():
    if row['CustomerCity'] == 'Kandy':
        df.loc[index,'Latitude']='7.2906'
        df.loc[index,'Longitude']='80.6336'
        df.loc[index,"Country"] = 'Srilanka'
        df.loc[index,"CountryCode"] = 'LK'

    elif row['CustomerCity'] == 'Colombo':
        df.loc[index,'Latitude']='6.874092'
        df.loc[index,'Longitude']='79.860497'
        df.loc[index,"Country"] = 'Srilanka'
        df.loc[index,"CountryCode"] = 'LK'

    elif row['CustomerCity'] == 'Chennai':
       	df.loc[index,'Latitude']='13.067439'
        df.loc[index,'Longitude']='80.237617'
        df.loc[index,"Country"] = 'India'
        df.loc[index,"CountryCode"] = 'IN'
    elif row['CustomerCity'] == 'Bangalore':
       	df.loc[index,'Latitude']='12.972442'
        df.loc[index,'Longitude']='77.580643'
        df.loc[index,"Country"] = 'India'
        df.loc[index,"CountryCode"] = 'IN'
    elif row['CustomerCity'] == 'Mumbai':
       	df.loc[index,'Latitude']='19.076090'
        df.loc[index,'Longitude']='72.877426'
        df.loc[index,"Country"] = 'India'
        df.loc[index,"CountryCode"] = 'IN'

    elif row['CustomerCity'] == 'Lagos':
       	df.loc[index,'Latitude']='6.465422'
        df.loc[index,'Longitude']='3.406448'
        df.loc[index,"Country"] = 'Nigeria'
        df.loc[index,"CountryCode"] = 'NG'

    elif row['CustomerCity'] == 'Frankfurt':
       	df.loc[index,'Latitude']='50.110924'
        df.loc[index,'Longitude']='8.682127'
        df.loc[index,"Country"] = 'Germany'
        df.loc[index,"CountryCode"] = 'DE'
        
#df["EID"] =  np.random.choice(15, 100000, p =[0.08,0.01,0.069,0.02,0.065,0.02,0.049,0.042,0.19,0.14,0.09,0.07,0.015,0.09,0.05])
#df['EID'].replace([0,1,2,3,4,5,6,7,8,9,10,14],['E00','E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11','E12','E13','E14'],inplace=True)
df["EID"] =  np.random.choice(15, 100000, p =[0.08,0.01,0.069,0.02,0.065,0.02,0.049,0.042,0.19,0.14,0.09,0.07,0.015,0.09,0.05])
df['EID'].replace([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14],['E00','E01','E02','E03','E04','E05','E06','E07','E08','E09','E10','E11','E12','E13','E14'],inplace=True)

for index , row in df.iterrows():
	if row['EID'] == 'E01':
		 df.loc[index,'Employee FirstName'] ='Robert'
		 df.loc[index,'Employee LastName'] ='Simsons'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='3.1'
					

	elif row['EID'] == 'E00':
		 df.loc[index,'Employee FirstName'] ='Julie'
		 df.loc[index,'Employee LastName'] ='Killonson'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='1.25'
		 df.loc[index,'Ratings'] ='3'

	elif row['EID'] == 'E02':
		 df.loc[index,'Employee FirstName'] ='Jenny'
		 df.loc[index,'Employee LastName'] ='Maddison'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='2.5'
		 df.loc[index,'Ratings'] ='3'

	elif row['EID'] == 'E03':
		 df.loc[index,'Employee FirstName'] ='Dmitrij'
		 df.loc[index,'Employee LastName'] ='Ilkovan'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='3'
         
	elif row['EID'] == 'E04':
		 df.loc[index,'Employee FirstName'] ='Tobias'
		 df.loc[index,'Employee LastName'] ='Helington'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='3'

	elif row['EID'] == 'E05':
		 df.loc[index,'Employee FirstName'] ='Sophia'
		 df.loc[index,'Employee LastName'] ='Anderson'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='3.5'

	elif row['EID'] == 'E06':
		 df.loc[index,'Employee FirstName'] ='Bill'
		 df.loc[index,'Employee LastName'] ='MCDermott'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.75'
		 df.loc[index,'Ratings'] ='3.6'

	elif row['EID'] == 'E07':
		 df.loc[index,'Employee FirstName'] ='Jermie'
		 df.loc[index,'Employee LastName'] ='Sims'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='2.7'

	elif row['EID'] == 'E08':
		 df.loc[index,'Employee FirstName'] ='Joe'
		 df.loc[index,'Employee LastName'] ='Dane'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='7.5'
		 df.loc[index,'Ratings'] ='3.9'

	elif row['EID'] == 'E09':
		 df.loc[index,'Employee FirstName'] ='Famis'
		 df.loc[index,'Employee LastName'] ='Lijie'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='8'
		 df.loc[index,'Ratings'] ='4.25'

	elif row['EID'] == 'E10':
		 df.loc[index,'Employee FirstName'] ='Betsy'
		 df.loc[index,'Employee LastName'] ='Domnik'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='9'
		 df.loc[index,'Ratings'] ='4.75'

	elif row['EID'] == 'E11':
		 df.loc[index,'Employee FirstName'] ='Jude'
		 df.loc[index,'Employee LastName'] ='Thomas'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='8'
		 df.loc[index,'Ratings'] ='4.5'

	elif row['EID'] == 'E12':
		 df.loc[index,'Employee FirstName'] ='Jill'
		 df.loc[index,'Employee LastName'] ='Diana'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='0.65'
		 df.loc[index,'Ratings'] ='4.1'

	elif row['EID'] == 'E13':
		 df.loc[index,'Employee FirstName'] ='Kate'
		 df.loc[index,'Employee LastName'] ='Hilton'
		 df.loc[index,'Employee Gender'] ='Female'
		 df.loc[index,'SaleXpLevel'] ='2.5'
		 df.loc[index,'Ratings'] ='3.25'

	elif row['EID'] == 'E14':
		 df.loc[index,'Employee FirstName'] ='Mathew'
		 df.loc[index,'Employee LastName'] ='Hardy'
		 df.loc[index,'Employee Gender'] ='Male'
		 df.loc[index,'SaleXpLevel'] ='1.5'
		 df.loc[index,'Ratings'] ='3.6'


print(df)


df['OrderNr'] = "ORD"+df['OrderDate'].str[:12].replace(to_replace='-',value='',regex=True) + df['CustomerID']
        
df.to_csv('DataFinal.csv', encoding='utf-8',header=True)

import sqlite3 as sql
data = pd.read_csv('DataFinal.csv')
conn = sql.connect('Sales.db')
df.to_sql('SalesCube', conn)
data = pd.read_sql('SELECT * FROM SalesCube', conn)
y2020 = pd.read_sql("SELECT CAST(QuantityPurchased as decimal) QuantityPurchased,OrderDate FROM SalesCube where strftime('%Y',date(OrderDate) )  == '2020'", conn)

y2019 = pd.read_sql("SELECT CAST(QuantityPurchased as decimal) QuantityPurchased,OrderDate FROM SalesCube where strftime('%Y',date(OrderDate) )  == '2019'", conn)
import matplotlib.pyplot as plt

ax2020 = y2020.plot(y= 'QuantityPurchased')
ax = y2019.plot(y='QuantityPurchased',color = 'red', ax=ax2020)
ax.legend(['2020','2019'])
conn.commit()
conn.close()
