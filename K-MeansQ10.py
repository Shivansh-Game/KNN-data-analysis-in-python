import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load the dataset
file_path = "final_weather_data.csv"  # Update the file path if necessary
df = pd.read_csv(file_path)

# Preprocess the data: drop categorical columns and the Date column
numeric_columns = df.drop(columns=['Date', 'Weather_Condition', 'Wind_Direction (Compass)'])
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_columns)
# Extract the initial centroids
record_01_jan_2015 = numeric_columns[df['Date'] == '01-Jan-2015'].values
record_02_jan_2015 = numeric_columns[df['Date'] == '02-Jan-2015'].values

# Stack the centroids for K-Means initialization
initial_centroids = np.vstack([record_01_jan_2015, record_02_jan_2015])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=2, init=initial_centroids, n_init=1, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Retrieve the updated cluster centers (scaled)
new_centroids = kmeans.cluster_centers_
new_centroids_original_scale = scaler.inverse_transform(new_centroids)

# Print results
print("New Cluster Centers (original scale):")
print(new_centroids_original_scale)
