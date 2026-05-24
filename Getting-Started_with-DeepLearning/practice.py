# import torch
# import torch.nn  as nn

# model = nn.Linear(1, 1)

# x = torch.tensor([[2.0]])
# y = torch.tensor([[4.0]])

# pred = model(x)

# loss_fn = nn.MSELoss()
# loss = loss_fn(pred, y)

# loss.backward()

# print(model.weight.grad)
# print(model.bias.grad)


import torch 
import torch.nn as nn
import torch.optim as optim

x = torch.tensor([[1.0],[2.0],[3.0],[4.0]])
y = torch.tensor([[2.0],[4.0],[6.0],[8.0]])

model = nn.Linear(1, 1)

loss_fn = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr = 0.1)

for epoch in range(10):
    pred = model(x)

    loss = loss_fn(pred, y)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    print(epoch, loss.item())

print("weight:",model.weight)
print("bias:",model.bias)

model.eval()

with torch.no_grad():
    new_x = torch.tensor([[10.0]])
    prediction = model(new_x)
    # print(f"prediction for 5 is:{prediction.item():.4f}")
    print(prediction)