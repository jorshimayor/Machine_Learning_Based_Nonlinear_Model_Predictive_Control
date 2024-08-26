def simulate_nmpc(model, initial_state, n_steps=100):
    states = [initial_state]
    for step in range(n_steps):
        current_state = np.array(states[-1]).reshape(1, 10, 3)  # reshape to match GRU input
        predicted_T = model.predict(current_state)
        optimal_control = optimize_control(predicted_T)  # Placeholder for NMPC optimization
        next_state = update_state(states[-1], optimal_control)
        states.append(next_state)
    return np.array(states)

# Example simulation
initial_state = X[0]  # Using the first sequence as initial state
simulated_states = simulate_nmpc(model, initial_state)
