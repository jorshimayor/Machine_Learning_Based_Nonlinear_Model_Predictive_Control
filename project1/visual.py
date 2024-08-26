import matplotlib.pyplot as plt

# Plot actual vs predicted values for Temperature and Concentration
plt.figure(figsize=(12, 6))

# Temperature
plt.subplot(1, 2, 1)
plt.plot(y_test[:, 0], label='Actual Temperature')
plt.plot(y_pred[:, 0], label='Predicted Temperature')
plt.xlabel('Sample')
plt.ylabel('Temperature')
plt.legend()
plt.title('Actual vs Predicted Temperature')

# Concentration
plt.subplot(1, 2, 2)
plt.plot(y_test[:, 1], label='Actual Concentration')
plt.plot(y_pred[:, 1], label='Predicted Concentration')
plt.xlabel('Sample')
plt.ylabel('Concentration')
plt.legend()
plt.title('Actual vs Predicted Concentration')

plt.tight_layout()
plt.show()
