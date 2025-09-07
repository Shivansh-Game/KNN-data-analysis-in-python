import pandas as pd
from sklearn.neighbors import NearestNeighbors

df = pd.read_csv("final_weather_data.csv")

num_c = ['Dew_Point (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Temperature (°C)', 'Visibility (km)']
df_num = df[num_c]

# Create a NearestNeighbors model with K=3
knn_model = NearestNeighbors(n_neighbors=3)

knn_model.fit(df_num)

new_record = [[13, 60, 1018, 20, 1]]
# Find the 3 nearest neighbors
distances, indices = knn_model.kneighbors(new_record)

# Print the indices of the nearest neighbors
print(indices)

print(df.iloc[indices[0]])

# Figuring out if Rain should be Present or not

print("It Will Rain" if df.iloc[indices[0]]["Rain_Presence"].mode()[0] == 0 else "It Will Not Rain")
