import pandas as pd 

df = pd.read_csv("final_weather_data.csv")
#1
print(df["Temperature (°C)"].idxmax())
print(df.iloc[130])
#2
print(df["Humidity (%)"].mean())
#3
print(df["Visibility (km)"].median())
#4
print(df["Wind_Direction (Compass)"].value_counts().idxmax())
#5
for i in df["Weather_Condition"].unique():
    print(i,df[df["Weather_Condition"] == i]["Temperature (°C)"].mean())