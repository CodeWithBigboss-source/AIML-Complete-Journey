# import torch
# import torch.nn as nn

# x = torch.tensor([[-10],[-2],[0],[4],[8]], dtype = torch.float32 )
# relu = nn.ReLU()
# output = relu(x)
# print("output: ",output)

import torch
import torch.nn as nn
import torch.optim as optim

# dataset
x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0]
])

y = torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0]
])

# neural network with ReLU
model = nn.Sequential(
    nn.Linear(1, 10),
    nn.ReLU(),
    nn.Linear(10, 1)
)

# loss function
loss_fn = nn.MSELoss()

# optimizer
optimizer = optim.SGD(model.parameters(), lr=0.01)

# training loop
for epoch in range(100):

    # forward propagation
    pred = model(x)

    # calculate loss
    loss = loss_fn(pred, y)

    # clear gradients
    optimizer.zero_grad()

    # backpropagation
    loss.backward()

    # gradient descent
    optimizer.step()

    print(epoch, loss.item())