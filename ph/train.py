import os
import torch
from data_processing import load_data
from model_lstm import LSTMModel  # Import LSTM model
from model_gru import GRUModel    # Import GRU model

# Get the base directory where the script is located
base_dir = os.path.dirname(__file__)

# Define file paths using the base directory
file_path1 = os.path.join(base_dir, "data", "training_data1.csv")
file_path2 = os.path.join(base_dir, "data", "training_data2.csv")
validation_path = os.path.join(base_dir, "data", "validation_data.csv")
test_path = os.path.join(base_dir, "data", "test_data.csv")

def train_model(model, train_loader, device, num_epochs=100, learning_rate=0.001):
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    
    model.to(device)
    
    for epoch in range(num_epochs):
        for i, (inputs, targets) in enumerate(train_loader):
            inputs, targets = inputs.to(device), targets.to(device)
            
            # Reshape inputs to be 3D (batch_size, sequence_length, input_size)
            inputs = inputs.unsqueeze(1)  # Adding sequence_length dimension
            
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            if (i+1) % 100 == 0:
                print(f'Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], Loss: {loss.item():.4f}')
    return model

def main():
    # Define hyperparameters
    input_size = 2  # Number of features ('time' and 'input')
    hidden_size = 64
    output_size = 1  # Predicting pH
    num_layers = 2
    num_epochs = 50
    learning_rate = 0.001

    # Set device to GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load datasets using the file paths
    train_loader1 = load_data(file_path1, batch_size=32)
    train_loader2 = load_data(file_path2, batch_size=32)
    validation_loader = load_data(validation_path, batch_size=32, shuffle=False)

    # Train LSTM model
    print("Training LSTM model...")
    lstm_model = LSTMModel(input_size, hidden_size, output_size, num_layers).to(device)
    trained_lstm = train_model(lstm_model, train_loader1, device, num_epochs, learning_rate)
    torch.save(trained_lstm.state_dict(), 'lstm_model.pth')

    # Train GRU model
    print("Training GRU model...")
    gru_model = GRUModel(input_size, hidden_size, output_size, num_layers).to(device)
    trained_gru = train_model(gru_model, train_loader2, device, num_epochs, learning_rate)
    torch.save(trained_gru.state_dict(), 'gru_model.pth')

if __name__ == "__main__":
    main()
