import torch
from torch import nn, optim
import torch.nn.functional as F
import torch.nn as nn 
from torch import nn, Tensor
import torch.utils.data as data_utils
import random
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class LSTMEncoder(nn.Module):
    def __init__(self, hidden_dim, layer_dim, lags, horizons, n_features):
        super(LSTMEncoder, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.lstm = nn.LSTM(n_features, hidden_dim, layer_dim, batch_first=True)

    def forward(self, x):
        out, (hidden, cell) = self.lstm(x)
        return hidden, cell
    
class LSTMDecoder(nn.Module):
    def __init__(self, hidden_dim, layer_dim, lags, horizons, n_features):
        super(LSTMDecoder, self).__init__()
        self.lstm = nn.LSTM(n_features, hidden_dim, layer_dim, batch_first=True)
        self.fc1 = nn.Linear(hidden_dim, 1)
        self.fc4 = nn.Linear(hidden_dim, n_features)

    def forward(self, x, hidden, cell):
        output, (hidden, cell) = self.lstm(x, (hidden, cell))
        out_1 = self.fc1(torch.squeeze(output))
        out_4 = self.fc4(hidden[-1])
        return out_1, out_4, hidden, cell
    
class LSTM_Seq2Seq(nn.Module):    
    def __init__(self,  hidden_dim, layer_dim, lags, horizons, n_features):
        super(LSTM_Seq2Seq, self).__init__()
        self.encoder = LSTMEncoder(hidden_dim, layer_dim, lags, horizons, n_features)
        self.decoder = LSTMDecoder(hidden_dim, layer_dim, lags, horizons, n_features)
        self.horizons = horizons
        
    def forward(self, src, trg, train):
        hidden, cell = self.encoder(src)
        outputs = torch.zeros(trg.shape[0], self.horizons).to(device)
        input_trg = src[:,src.shape[1]-1:src.shape[1],:]
        start = 0
        end = 1
        if(train == True):            
            for t in range(0, self.horizons):
                out_1, out_4, hidden, cell = self.decoder(input_trg, hidden, cell)
                outputs[:,start:end] = out_1
                if random.random() < 0.4:
                    input_trg = trg[:,start:end,:]
                else:
                    input_trg = out_4.unsqueeze(1)
                start = end 
                end = end + 1
        elif(train == False):
            for t in range(0, self.horizons):
                out_1, out_4, hidden, cell = self.decoder(input_trg, hidden, cell)
                outputs[:,start:end] = out_1
                input_trg = out_4.unsqueeze(1)
                start = end 
                end = end + 1
        return outputs