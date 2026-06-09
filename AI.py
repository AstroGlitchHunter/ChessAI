import torch
import torch.nn as nn
import torch.optim as optim
import random
from Dataset import data_X, data_Y

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

X = torch.tensor(data_X, dtype=torch.float32).to(device)
y = torch.tensor(data_Y, dtype=torch.float32).to(device)



class ChessNet(nn.Module):
    def __init__(self):
        super(ChessNet, self).__init__()

        self.net = nn.Sequential(
            nn.LayerNorm(10),
            nn.Linear(10, 128),
            nn.GELU(),
            nn.Linear(128, 64),
            nn.GELU(),
            nn.Linear(64, 1),

        )

    def forward(self, x):
        raw = self.net(x)
        return torch.sigmoid(raw * 10.0)


if __name__ == "__main__":

    model = ChessNet().to(device)
    optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss()


    model.train()
    for epoch in range(2500):
        prediction = model.net(X)
        loss = criterion(prediction, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if epoch % 100 == 0:
            print(f'Epoch: {epoch}, Loss: {loss.item():.4f}')

    total_error = 0
    model.eval()
    with torch.no_grad():
        prediction = model(X)
        for i, c in enumerate(prediction):
            pred_val = c.item()
            real_val = y[i, 0]
            mae_diff = abs(pred_val - real_val)
            total_error += mae_diff
            print(f'Predict for value №{i + 1}: {c.item()}. Absolute Error: {mae_diff * 100}%')

    average_error = (total_error / len(data_Y)) * 100
    print(f'Average Error: {average_error:.2f}%')
    torch.save(model.state_dict(), 'chess_net_weights.pth')
    print("Created chess_net_weights.pth📗")