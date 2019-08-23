#Lab 2: Basic csv read-write and data frame using pandas library 
import pandas as pd
print(type(pd.read_csv))

help(pd)
#df=pd.read_csv('F:\\Numerical_Computing\Lab_10\example.csv', header=0, nrows=100)
df=pd.read_csv('C:\\Users\ISPA-PC TEACHER\Desktop\Statistical_Inference_and_Data_Mining\Labs\Lab_2\example.csv',header=-1)


print('after row')
print(df[2:])
# print('print till specific row')
# c=df.iloc[2]
#print(c)
print('print before row')
c=df.iloc[:3]
print(c)
print('by row and column')
c=df.iloc[2,1]
print(c)
print('print specific column')
c=df.iloc[:,1]
print(c)


print('basic statistics related to numerical columns before change')
print(df.describe())

df.iloc[0,1]=50  #changing data first row and second column
df.iloc[23,0]=90  # 24th row and first column
print('dataframe after value change')
c=df
print(c)
print(df)
df.to_csv('C:\\Users\ISPA-PC TEACHER\Desktop\Statistical_Inference_and_Data_Mining\Labs\Lab_2\example_pandas_df_out.csv')

print('basic statistics related to numerical columns after change')
print(df.describe())
# 


print(df)
