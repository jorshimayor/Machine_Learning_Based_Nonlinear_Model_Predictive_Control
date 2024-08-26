from sklearn.preprocessing import MinMaxScaler
from pandas import pd

# Load data
data = pd.read_csv('nmpc_data.csv')

# Normalize the input and target variables
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data)

# Convert back to DataFrame for easier manipulation
scaled_df = pd.DataFrame(scaled_data, columns=data.columns)

# Save the normalized data
scaled_df.to_csv('nmpc_data_scaled.csv', index=False)
