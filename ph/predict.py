import os
import torch
from model_lstm import LSTMModel
from model_gru import GRUModel
from data_processing import load_data

def predict(model, test_loader, device):
    model.eval()
    predictions = []
    with torch.no_grad():
        for inputs, _ in test_loader:
            inputs = inputs.to(device)
            
            # Reshape inputs to add a sequence length dimension
            inputs = inputs.unsqueeze(1)  # [batch_size, sequence_length=1, input_size]
            
            outputs = model(inputs)
            predictions.append(outputs.cpu().numpy())
    return predictions

def main():
    # Get the base directory where the script is located
    base_dir = os.path.dirname(__file__)

    # Define the correct file path for the test data
    test_path = os.path.join(base_dir, 'data', 'test_data.csv')

    # Set device to GPU if available, otherwise use CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    # Load the test data
    test_loader = load_data(test_path, batch_size=1, shuffle=False)

    # Load and test LSTM model
    lstm_model = LSTMModel(input_size=2, hidden_size=64, output_size=1, num_layers=2).to(device)
    lstm_model.load_state_dict(torch.load('lstm_model.pth', map_location=device))  # Load model to correct device
    lstm_predictions = predict(lstm_model, test_loader, device)
    print("LSTM Predictions:", lstm_predictions)

    # Load and test GRU model
    gru_model = GRUModel(input_size=2, hidden_size=64, output_size=1, num_layers=2).to(device)
    gru_model.load_state_dict(torch.load('gru_model.pth', map_location=device))  # Load model to correct device
    gru_predictions = predict(gru_model, test_loader, device)
    print("GRU Predictions:", gru_predictions)

if __name__ == "__main__":
    main()
