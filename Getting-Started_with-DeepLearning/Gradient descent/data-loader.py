import torch
from torch.utils.data import TensorDataset, DataLoader
import torch.nn as nn
import torch.optim as optim

# -----------------------------
# Step 1 — Create Dataset
# -----------------------------

x = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y = torch.tensor([
    [2.0],
    [4.0],
    [6.0],
    [8.0],
    [10.0],
    [12.0]
])

# -----------------------------
# Step 2 — Train/Test Split
# -----------------------------

x_train = x[:4]
y_train = y[:4]

x_test = x[4:]
y_test = y[4:]

# -----------------------------
# Step 3 — Create Dataset Object
# -----------------------------

train_dataset = TensorDataset(x_train, y_train)

# -----------------------------
# Step 4 — Create DataLoader
# -----------------------------

train_loader = DataLoader(
    train_dataset,
    batch_size=2,
    shuffle=True
)

# -----------------------------
# Step 5 — Create Model
# -----------------------------

model = nn.Linear(1,1)

# -----------------------------
# Step 6 — Loss Function
# -----------------------------

loss_fn = nn.MSELoss()

# -----------------------------
# Step 7 — Optimizer
# -----------------------------

optimizer = optim.SGD(
    model.parameters(),
    lr=0.01
)

# -----------------------------
# Step 8 — Training Loop
# -----------------------------

for epoch in range(20):

    for batch_x, batch_y in train_loader:

        print("Batch Inputs:")
        print(batch_x)

        # Forward Propagation
        pred = model(batch_x)

        # Calculate Loss
        loss = loss_fn(pred, batch_y)

        # Clear Old Gradients
        optimizer.zero_grad()

        # Backpropagation
        loss.backward()

        # Gradient Descent
        optimizer.step()

    print("Epoch:", epoch)
    print("Loss:", loss.item())
    print("-------------------")

# -----------------------------
# Step 9 — Testing
# -----------------------------

with torch.no_grad():

    pred = model(x_test)

    print("Test Predictions:")
    print(pred)