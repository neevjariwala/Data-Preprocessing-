import pandas as pd
import numpy as np

df=pd.read_csv("messy_employee_data.csv",na_values=["nan","NAN","unknown","N/A","NaN"])
df.dropna(subset=["employee_id"],inplace=True)
df.drop_duplicates(subset=["employee_id"],keep="first",inplace=True)
df["salary"]=df["salary"].astype(str).str.replace("$","",regex=False).str.replace(",","",regex=False).str.strip()
df["salary"]=pd.to_numeric(df["salary"],errors="coerce")
mean_salary=round(df["salary"].mean())
df["salary"].fillna(mean_salary)
df["salary"]=df["salary"].astype("Int64")
print(df.isnull().sum())
print(df.dtypes)

# mean_salary=df["salary"].mean()
# df["salary"].fillna(mean_salary,inplace=True)
# print(df)