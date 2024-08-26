import numpy as np
import pandas as pd

# Define time range and initialize variables
time_steps = 1000
np.random.seed(42)  # For reproducibility

# Generate synthetic data for past system states and control inputs
time = np.linspace(0, 10, time_steps)
C_A = np.sin(0.5 * time) + 0.1 * np.random.randn(time_steps)  # Reactant concentration
T = 300 + 10 * np.sin(0.2 * time) + 2 * np.random.randn(time_steps)  # Reactor temperature
T_c = 290 + 5 * np.random.randn(time_steps)  # Cooling temperature
q = 1.5 + 0.05 * np.random.randn(time_steps)  # Feed rate

# Combine data into a DataFrame
data = pd.DataFrame({
    'time': time,
    'C_A': C_A,
    'T': T,
    'T_c': T_c,
    'q': q
})

# Save to a CSV file
data.to_csv('data.csv', index=False)