import torch
import torch.nn as nn
import torch.optim as optim

x = torch.tensor([[1],[2],[3],[4]], dtype = torch.float32)
y = torch.tensor([[2],[4],[6],[8]], dtype = torch.float32)

model = nn.Linear(1, 1)

loss_fn = nn.MSELoss()

optimizer = optim.SGD(model.parameters(), lr = 0.01)

for epoch in range(100):
    pred = model(x)

    loss = loss_fn(pred, y)

    optimizer.zero_grad()

    print("weight:",model.weight.grad)

    loss.backward()

    optimizer.step()

    print(f"epoch:{epoch} loss:{loss.item()})

model.eval()
new_x = torch.tensor([[40.0]])
new_pred = model(new_x)
print("new pred result:",new_pred)