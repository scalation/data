import torch
from torch import nn
import math

class FFNN(nn.Module):
    def __init__(self,units_layer1,units_layer2,lags,horizons,n_features):
        super(FFNN, self).__init__()
        self.linear1 = nn.Linear(lags*n_features, units_layer1)
        self.linear2 = nn.Linear(units_layer1, units_layer2)
        self.linear3 = nn.Linear(units_layer2, horizons*n_features)  
        self.horizons = horizons
        self.n_features = n_features
    def forward(self, src, trg, train):
        src = torch.flatten(src, start_dim=1)
        src = torch.relu(self.linear1(src))
        src = torch.relu(self.linear2(src))
        output = self.linear3(src)
        output = torch.reshape(output, (output.shape[0],self.horizons, self.n_features))
        return output[:,:,0]