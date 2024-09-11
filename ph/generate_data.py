import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
q_acid = 0.5  # flow rate of acid (L/s)
q_base = 0.4  # flow rate of base (L/s)
q_buffer = 0.3  # flow rate of buffer (L/s)
V = 1.0  # volume of the tank (L)

# Initial pH level in the tank
pH_initial = 7.0

# Model for pH dynamics
def ph_neutralization(pH, t, q_acid, q_base, q_buffer):
    # Simplified rate of pH change (for example purposes)
    rate_of_change = q_acid * (7 - pH) - q_base * (pH - 7) + q_buffer
    return rate_of_change / V

# Time points (e.g., simulate over 2000 time steps)
t = np.linspace(0, 2000, 2000)

# Simulate pH dynamics
pH_values = odeint(ph_neutralization, pH_initial, t, args=(q_acid, q_base, q_buffer))

# Plot the generated data
plt.plot(t, pH_values)
plt.xlabel('Time')
plt.ylabel('pH level')
plt.title('Simulated pH Neutralization Process')
plt.show()

# Save the data to a CSV file
data = np.column_stack((t, pH_values))
np.savetxt('ph_simulated_data.csv', data, delimiter=',', header='time,pH', comments='')
