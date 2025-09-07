import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


file_path = "final_weather_data.csv"
df = pd.read_csv(file_path)

record_01_jan_2015 = df.loc[df['Date'] == '01-Jan-2015'].drop(columns=['Weather_Condition', 'Wind_Direction (Compass)', 'Date'])
record_12_jan_2016 = df.loc[df['Date'] == '12-Jan-2016'].drop(columns=['Weather_Condition', 'Wind_Direction (Compass)', 'Date'])

distance = np.sqrt(np.sum((record_01_jan_2015.values - record_12_jan_2016.values) ** 2))
print(f"Distance: {distance}")

record_02_jan_2015 = df.loc[df['Date'] == '02-Jan-2015'].drop(columns=['Weather_Condition', 'Wind_Direction (Compass)', 'Date'])
record_04_jan_2015 = df.loc[df['Date'] == '04-Jan-2015'].drop(columns=['Weather_Condition', 'Wind_Direction (Compass)', 'Date'])

if np.sqrt(np.sum((record_01_jan_2015.values - record_04_jan_2015.values) ** 2)) < np.sqrt(np.sum((record_02_jan_2015.values - record_04_jan_2015.values) ** 2)):
    print("It is assigned to C1")
else:
    print("C2")
