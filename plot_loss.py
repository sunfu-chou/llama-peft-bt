import matplotlib.pyplot as plt
import pandas as pd

# Load the CSV files
eval_loss_path = "./eval_loss.csv"
train_loss_path = "./train_loss.csv"

eval_loss_df = pd.read_csv(eval_loss_path)
train_loss_df = pd.read_csv(train_loss_path)

# Extract the relevant columns
steps = eval_loss_df["Step"]
eval_loss = eval_loss_df["./output-test-3 - eval/loss"]
train_loss = train_loss_df["./output-test-3 - train/loss"]

# Plot the loss curves
plt.figure(figsize=(10, 6))
plt.plot(steps//2+1, train_loss, label='Train Loss')
plt.plot(steps//2+1, eval_loss, label='Eval Loss')
plt.xlabel('Step', fontsize=20)
plt.ylabel('Loss', fontsize=20)
plt.title('Train and Eval Loss Curves', fontsize=20)
plt.legend(fontsize=20)
plt.grid(True)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.savefig('loss_curve.png')
plt.show()
