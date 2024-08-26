import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense

# Load data
data = pd.read_csv('data.csv')
features = data[['C_A', 'T_c', 'q']].values
target = data['T'].values

# Create time-series sequences
time_steps = 10
X, y = [], []
for i in range(len(features) - time_steps):
    X.append(features[i:i+time_steps])
    y.append(target[i+time_steps])
X, y = np.array(X), np.array(y)

# Build GRU model
model = Sequential([
    GRU(64, activation='tanh', input_shape=(X.shape[1], X.shape[2])),
    Dense(32, activation='relu'),
    Dense(1)  # Predict temperature T
])

# Compile and train the model
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=50, batch_size=32, validation_split=0.2)
