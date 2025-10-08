import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Läs in data
data = pd.read_csv("Labs/Labb 3/unlabelled_data.csv", names=["x", "y"])
x=np.array(data["x"])
y=np.array(data["y"])

# Funktion som klassificerar en punkt
def classify_point (x, y, k, m):
    y_line = k * x + m
    return 1 if y > y_line else 0

k = -1 # lutning på linjen
m_values = [-0.5, -0.2, 0, 0.2, 0.5] # olika m-värden

for m in m_values: # loopa igenom alla m-värden
    data['label'] = data.apply(lambda row: classify_point(row['x'], row['y'], k, m), axis=1)
    above = sum(data['label'] == 1)
    below = sum(data['label'] == 0)
    print(f"Linje: y = {k}x + {m}, ovanför={above}, nedanför={below}")

m = 0 # välj det m som gav bäst balans

# Klassificera alla punkter
data ['label'] = data.apply(lambda row: classify_point(row['x'], row['y'], k, m), axis=1)

# Spara till labelled_data.csv
data.to_csv("Labs/Labb 3/labelled_data.csv", index=False)

print("Filen labelled_data.csv har skapats")

# Skapa koordinater för att rita upp linjen i grafen
x_line = np.linspace(min(x), max(x), 100)
y_line = k * x_line + m

# Rita figur med färgade punkter beroende på klass
colors = data['label'].map({0: 'pink', 1: 'purple'})
plt.scatter(data['x'], data['y'], c=colors)
plt.plot(x_line, y_line, color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Klassificering av punkter')
plt.show()