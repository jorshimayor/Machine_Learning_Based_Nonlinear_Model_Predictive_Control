# **Machine Learning-Based Nonlinear Model Predictive Control using GRU**

## **Overview**

This project is focused on implementing a Machine Learning-Based Nonlinear Model Predictive Control (NMPC) system using a Gated Recurrent Unit (GRU) neural network. The project is built around a Continuous Stirred-Tank Reactor (CSTR) system, a common chemical reactor model used in various industrial processes.

### **Gated Recurrent Unit (GRU) Neural Networks**

Gated Recurrent Units (GRUs) are a type of Recurrent Neural Network (RNN) that are particularly well-suited for processing sequential data. Unlike traditional RNNs, GRUs can capture long-term dependencies more effectively, making them highly useful in time-series forecasting tasks.

#### **Why GRU for NMPC?**

- **Time-Series Prediction**: GRUs are designed to handle sequential data, making them ideal for predicting the future states of a system based on its past states and control inputs. In the context of NMPC, GRUs help predict future system states, which the controller then uses to optimize the control actions.
  
- **Efficiency**: GRUs are computationally less expensive than their counterparts, such as Long Short-Term Memory (LSTM) networks, while still offering comparable performance. This efficiency is crucial in real-time control systems where quick decisions are necessary.

- **Handling Nonlinearities**: The GRU model can capture the nonlinear behavior of the CSTR system, providing more accurate predictions that are essential for effective control.

### **Project Structure**

This project is structured into several key steps:

1. **Data Generation**:
   - Historical data is generated to represent past system states (e.g., concentration and temperature in the CSTR) and control inputs (e.g., cooling temperature and feed rate).
   - This data is stored in a CSV file (`data.csv`), which is used for training the GRU model.

2. **GRU Model Training**:
   - A GRU model is trained on the historical data to learn the relationship between past states, control inputs, and future states.
   - The trained model is then used to predict future system states based on new control inputs.

3. **Nonlinear Model Predictive Control (NMPC)**:
   - The GRU model's predictions are integrated into an NMPC framework.
   - The NMPC optimizes the control inputs (cooling temperature, feed rate) to achieve the desired reactor states (e.g., temperature and concentration).

4. **Simulation**:
   - The system is simulated over a defined period to observe the performance of the NMPC using the GRU model.
   - This simulation helps to visualize how well the system tracks desired setpoints and responds to disturbances.

5. **Evaluation**:
   - The performance of the control strategy is evaluated using metrics like Mean Squared Error (MSE) to quantify the accuracy of tracking the desired states.

### **Running the Project**

To run the project, follow these steps:

#### **1. Set Up Your Environment**

- **Install Python**: Make sure Python is installed on your machine.
- **Create a Virtual Environment** (optional but recommended):

  ```bash
  python -m venv myenv
  source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
  ```

- **Install Required Libraries**:

  ```bash
  pip install numpy pandas matplotlib tensorflow scikit-learn
  ```

#### **2. Generate Historical Data**

- Save the code for generating historical data in a file named `generate_data.py`.
- Run the script to create the `data.csv` file:

  ```bash
  python generate_data.py
  ```

#### **3. Train the GRU Model**

- Save the GRU model training code in a file named `train_gru.py`.
- Run the script to train the GRU model:

  ```bash
  python train_gru.py
  ```

#### **4. Simulate the System**

- Save the simulation code in a file named `simulate_nmpc.py`.
- Run the script to simulate the system and visualize the results:

  ```bash
  python simulate_nmpc.py
  ```

#### **5. Evaluate the Results**

- Save the evaluation code in a file named `evaluate_nmpc.py`.
- Run the script to evaluate the performance:

  ```bash
  python evaluate_nmpc.py
  ```

### **Summary**

This project demonstrates the integration of machine learning, specifically GRU networks, into a Nonlinear Model Predictive Control framework for a CSTR system. By following the steps outlined in this README, you can replicate the process and gain insights into how GRUs can be used to enhance the performance of control systems.
