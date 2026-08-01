import kagglehub
import pandas as pd
import numpy as pn

# Download latest version
# path = kagglehub.dataset_download("ariyoomotade/netflix-data-cleaning-analysis-and-visualization")

# print("Path to dataset files:", path)
df = pd.read_csv("C:\\Users\\admin\\.cache\\kagglehub\\datasets\\ariyoomotade\\netflix-data-cleaning-analysis-and-visualization\\versions\\1\\netflix1.csv")
# print(df.head())
# print(df.dtypes)
df["date_added"]=pd.to_datetime(df["date_added"])
print(df.dtypes)
