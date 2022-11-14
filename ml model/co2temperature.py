import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

co=pd.read_csv('owid-co2-data.csv')
temp=pd.read_csv('city_temperature.csv')


temp.columns=temp.columns.map(lambda x: x.lower())
df=pd.merge(co,temp,on=['country','year'])

df.drop_duplicates()

fit1=sm.formula.ols('avgtemperature~co2',data=df).fit()
print(fit1.params)
print(fit1.summary())


fit2=sm.formula.ols('avgtemperature~co2+country+co2*country',data=df).fit()
print(fit2.params)
print(fit2.summary())



