# import torch
# import torch.nn as nn

# x = torch.tensor([[2.0]])

# layer = nn.Linear(1,1)

# y = layer(x)
# print(y)


import torch
import torch.nn as nn

layer = nn.Linear(1, 1)

x = torch.tensor([[5.0]])

y = layer(x)

print(y)
