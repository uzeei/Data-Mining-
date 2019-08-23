# -*- coding: utf-8 -*-
#Lab 2: SCreating data using dictionary and saving in csv using pandas
import pandas as pd

data = {'Country': ['Belgium', 'India', 'Pakistan'],
'Capital': ['Brussels', 'New Delhi', 'Islamabad'],
'Population': [11190846, 1303171035, 212847528]}

df = pd.DataFrame(data,columns=['Country', 'Capital', 'Population'])

print(help(df.insert))
continent=['Europe','Asia','Asia']
df.insert(3,'Continent',continent)


df.to_csv('C:\\Users\ISPA-PC TEACHER\Desktop\Statistical_Inference_and_Data_Mining\Labs\Lab_2\country.csv')
print(df)
print(df.describe())
print('data farame to dictionary')
dicdf=dict(df)
print(dicdf.keys())

print(dicdf)



