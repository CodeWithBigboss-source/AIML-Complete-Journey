# import torch 
# import torch.nn as nn

# loss_fn = nn.MSELoss()

# pred = torch.tensor([7.0])
# target = torch.tensor([10.0])

# loss = loss_fn(pred,target)
# print(loss)


import torch
import torch.nn as nn
# mean squarred difference = (pred - actual)pow2
loss_fn = nn.MSELoss()

pred = torch.tensor([6.0])
actual = torch.tensor([10.0])

loss = loss_fn(pred, actual)
print(loss)