from collections import namedtuple
import sys
import torch
import torch.nn as nn
import torch.nn.utils
import torch.nn.functional as F
#import matplotlib.pyplot as plt

class Net(nn.Module):
    def __init__(self, vocab_size, dropout=0.2):
        super(Net, self).__init__()

        self.linear1 = nn.Linear(vocab_size, 50)
        self.relu1 = nn.ReLU()
        self.dropout = nn.Dropout(dropout)
        self.linear2 = nn.Linear(50, 100)
        self.prelu = nn.PReLU(1)
        self.out = nn.Linear(100, 1)
        self.out_activation = nn.Sigmoid()

    def forward(self, input) -> torch.Tensor:
        a1 = self.linear1(input)
        h1 = self.relu1(a1)
        h1_dropout = self.dropout(h1)
        a2 = self.linear2(h1_dropout)
        h2 = self.prelu(a2)
        a3 = self.out(h2)
        y = self.out_activation(a3)
        return y