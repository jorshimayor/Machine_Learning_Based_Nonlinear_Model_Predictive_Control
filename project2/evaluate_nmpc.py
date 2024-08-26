import matplotlib.pyplot as plt

# Plot actual vs. predicted temperatures
plt.figure(figsize=(10, 6))
plt.plot(data['time'][:n_steps], simulated_states[:, 1], label='Predicted Temperature')
plt.plot(data['time'][:n_steps], data['T'][:n_steps], label='Actual Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (K)')
plt.legend()
plt.show()
