from gekko import GEKKO

# Initialize GEKKO
m = GEKKO(remote=False)
m.time = np.linspace(0, 1, 11)  # time horizon

# Variables
T = m.Var(value=300)  # Reactor temperature
Ca = m.Var(value=0.5)  # Concentration

# Parameters
Cooling_Temp = m.MV(value=280)  # Manipulated variable (cooling temperature)
Cooling_Temp.STATUS = 1  # Allow optimization

# Define model equations based on FNN predictions
def predict_next_state(current_state):
    return model.predict(current_state.reshape(1, -1)).flatten()

# Use the model's predictions to define the system's behavior
for i in range(1, len(m.time)):
    state = np.array([Cooling_Temp.value, T.value, Ca.value])
    T_next, Ca_next = predict_next_state(state)
    m.Equation(T.dt() == T_next - T.value)
    m.Equation(Ca.dt() == Ca_next - Ca.value)

# Define the optimization objective

m.Obj((T - 310)**2)  # Target temperature (310 K)

# Solver options
m.options.IMODE = 6  # Dynamic optimization
m.solve(disp=True)

# Retrieve results
T_res = T.value
Ca_res = Ca.value
Cooling_Temp_res = Cooling_Temp.value

# Plot the results
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(m.time, T_res, label='Temperature')
plt.xlabel('Time')
plt.ylabel('Temperature (K)')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(m.time, Ca_res, label='Concentration')
plt.xlabel('Time')
plt.ylabel('Concentration')
plt.legend()

plt.tight_layout()
plt.show()
