import numpy as np
import pandas as pd
from gekko import GEKKO

# Initialize GEKKO model
m = GEKKO(remote=False)

# Time vector
time = np.linspace(0, 10, 100)  # 10 seconds, 100 samples
m.time = time

# Variables (example: temperature and concentration)
T = m.Var(value=300)  # Initial temperature
Ca = m.Var(value=0.5)  # Initial concentration

# Control input (example: cooling temperature)
Cooling_Temp = m.Param(value=280)

# Differential equations (example)
k = 0.1  # Reaction rate constant
m.Equation(T.dt() == -k*(T - Cooling_Temp))
m.Equation(Ca.dt() == -k*Ca)

# Simulate
m.options.IMODE = 4  # Dynamic simulation
m.solve(disp=False)

# Collect data
data = {
    'Time': time,
    'Cooling_Temp': Cooling_Temp.value * np.ones_like(time),  # Assume constant for simplicity
    'Initial_Temperature': T.value,
    'Initial_Concentration': Ca.value,
    'Next_Temperature': np.roll(T.value, -1),  # Shifted to represent next state
    'Next_Concentration': np.roll(Ca.value, -1)  # Shifted to represent next state
}

df = pd.DataFrame(data)
df = df[:-1]  # Remove the last row due to rolling
df.to_csv('nmpc_data.csv', index=False)
