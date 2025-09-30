import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
import os 
print(os.getcwd())
sys.stdout.flush()

def load_data_points(data_points):
    points = []
    with open (data_points, "r") as file:
        next(file)

        for line in file:
            line = line.strip().split(",")
            if len(line) == 3:
                x, y, label = line
                points.append((float(x), float(y), int(label)))
    return points



def load_test_points(test_points):
    points = []
    with open(test_points, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            line = line.replace("(", "").replace(")", "")
            x, y = line.split(",")
            points.append((float(x), float(y)))
    return points

data_points = load_data_points("Labs/datapoints.txt")
test_points = load_test_points("Labs/testpoints.txt")

print(test_points[0])
