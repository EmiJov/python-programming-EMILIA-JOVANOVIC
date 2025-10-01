import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Labs/Labb 3/unlabelled_data.csv", names=["x", "y"])
x=np.array(data["x"])
y=np.array(data["y"])

k = -1
m = -0

x_line = np.linspace(min(x), max(x), 100)
y_line = k * x_line + m

plt.scatter(x, y)
plt.plot(x_line, y_line, color='red') # linjen y = x
plt.show()

# Funktion som klassificerar en punkt
def classify_point (x, y, k, m):
    y_line = k * x + m
    return 1 if y > y_line else 0

# Klassificera alla punkter
data ['label'] = data.apply(lambda row: classify_point(row['x'], row['y'], k, m), axis=1)

# Spara till labelled_data.csv
data.to_csv("Labs/Labb 3/labelled_data.csv", index=False)

print("Filen labelled_data.csv har skapats")