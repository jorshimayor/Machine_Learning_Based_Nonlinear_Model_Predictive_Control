import torch
import matplotlib.pyplot as plt
import numpy as np

# Load the simulated states (or use your own tensor directly)
simulated_states = torch.load('simulated_states.pt')

# Assuming you have real outputs (target values) to compare against
# Replace this with your actual data for real_output
real_output = np.random.rand(simulated_states.size(0), 1)  # Placeholder data

# Convert to NumPy arrays for plotting
predicted_output = simulated_states.numpy()
predicted_output = predicted_output[:, 0, 0]  # Extract the specific variable you're interested in

# Plot Prediction vs Real Output
plt.figure(figsize=(10, 6))
plt.plot(real_output, label='Real output', color='orange')
plt.plot(predicted_output, label='Prediction', linestyle='--', color='black')
plt.xlabel('Timestep')
plt.ylabel('Variable Value')
plt.title('Prediction on test set')
plt.legend()
plt.grid(True)
plt.show()

# Calculate the prediction error
prediction_error = real_output - predicted_output.reshape(-1, 1)

# Plot Prediction Error
plt.figure(figsize=(10, 6))
plt.plot(prediction_error, label='Error (Real - Prediction)', color='blue')
plt.xlabel('Timestep')
plt.ylabel('Error')
plt.title('Prediction error on test set')
plt.grid(True)
plt.show()
