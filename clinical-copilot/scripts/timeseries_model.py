# scripts/timeseries_model.py
import torch
import torch.nn as nn

class SepsisLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(SepsisLSTM, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # x shape: (batch_size, sequence_length, input_size)
        lstm_out, _ = self.lstm(x)
        last_hidden_state = lstm_out[:, -1, :]
        out = self.fc(last_hidden_state)
        prediction = self.sigmoid(out)
        return prediction
