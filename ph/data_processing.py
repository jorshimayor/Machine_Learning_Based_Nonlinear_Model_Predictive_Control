import torch
from torch.utils.data import Dataset, DataLoader
import pandas as pd

class pHNeutralizationDataset(Dataset):
    def __init__(self, csv_file):
        data = pd.read_csv(csv_file)
        self.inputs = data[['time', 'input_mL_s']].values  # Using 'time' and 'input' as features
        self.targets = data['pH'].values.reshape(-1, 1)    # pH values as target

    def __len__(self):
        return len(self.inputs)

    def __getitem__(self, idx):
        return torch.tensor(self.inputs[idx], dtype=torch.float32), torch.tensor(self.targets[idx], dtype=torch.float32)

def load_data(csv_file, batch_size=32, shuffle=True):
    dataset = pHNeutralizationDataset(csv_file)
    return DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
