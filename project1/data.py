import numpy as np
import pandas as pd

# Load your data (assume you have a CSV file with the data)
data = pd.read_csv('nmpc_data.csv')

# Extract input features (e.g., Cooling_Temp, initial states) and target variables (e.g., Temperature, Concentration)
X = data[['Cooling_Temp', 'Initial_Temperature', 'Initial_Concentration']].values
y = data[['Temperature', 'Concentration']].values

# Split the data into training and testing sets
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
