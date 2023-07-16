# -*- coding: utf-8 -*-
"""Task 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1py2lNN02MeVUEYyqlhn09VvGrlTTtktv
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error

df=pd.read_excel("/content/Regression Data.xlsx")
df

#Linear regression using Volume
x=df[['Volume']]
y=df['CO2']
plt.scatter(x,y)
plt.show()

model = LinearRegression()
model.fit(x, y)
y_pred=model.predict(x)

plt.title("CO2 wrt volume")
plt.xlabel('Volume')
plt.ylabel('CO2')
plt.scatter(x,y,label='actual_data',color='purple',alpha=0.5)
plt.plot(x,y_pred,c='cyan',label='best')
plt.legend()
plt.show()

r2_score(y,y_pred)

#Linear regression using Weight
x=df[['Weight']]
y=df['CO2']
plt.scatter(x,y)

model = LinearRegression()
model.fit(x, y)
y_pred=model.predict(x)

plt.title("CO2 wrt weight")
plt.xlabel('Weight')
plt.ylabel('CO2')
plt.scatter(x,y,label='actual_data',color='purple',alpha=0.5)
plt.plot(x,y_pred,c='cyan',label='best')
plt.legend()
plt.show()

r2_score(y,y_pred)

#MULTIPLE REGRESSION
x=df[['Weight','Volume']]
y=df['CO2']

model = LinearRegression()
model.fit(x, y)
y_pred=model.predict(x)

df1=pd.DataFrame({'Actual':y,'Predicted':y_pred})
df1

df1.plot(figsize=(20,8),kind='bar')
plt.show()

r2_score(y,y_pred)