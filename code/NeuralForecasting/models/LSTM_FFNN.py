import torch
from torch import nn
import math

class LSTM_FFNN(nn.Module):
    def __init__(self, hidden_dim, layer_dim, lags, horizons, n_features):
        super(LSTM_FFNN, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.lags = lags
        self.horizons = horizons
        self.n_features = n_features

        self.lstm = nn.LSTM(n_features, hidden_dim, layer_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, horizons)
    def forward(self, src, trg, train):
        out, (hidden, cell) = self.lstm(src)
        output = self.fc(hidden[-1])
        return output

"""
class LSTM_FFNN(nn.Module):
    def __init__(self, hidden_dim, layer_dim, lags, horizons, n_features):
        super(LSTM_FFNN, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.lags = lags
        self.horizons = horizons
        self.n_features = n_features

        self.lstm = nn.LSTM(n_features, hidden_dim, layer_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, horizons*n_features)
    def forward(self, src, trg, train):
        out, (hidden, cell) = self.lstm(src)
        out = self.fc(hidden[-1])
        output = torch.reshape(out, (out.shape[0],self.horizons, self.n_features))
        return output[:,:,0]
"""