import torch
import torch.nn as nn
import torch.optim as optim

#data
x = torch.tensor([[1.0],[2.0],[3.0]])
y = torch.tensor([[2.0],[4.0],[6.0]])

# model
model = nn.Linear(1,1)

loss_fn = nn.MSELoss()

# optimizer gradient descent
optimizer = optim.SGD(model.parameters(), lr=0.01)

# training loop
for epoch in range(100):

    # forward propagation
    pred = model(x)

    # loss calculation
    loss = loss_fn(pred, y)

    # clear old gradients
    optimizer.zero_grad()

    # backpropagation
    loss.backward()

    # gradient desent update
    optimizer.step()

    print(epoch, loss.item())