import math
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Läs in datapoints (width, height, label)

data_path = "Labs/datapoints.txt"
test_path = "Labs/testpoints.txt"

def load_data_points(data_path):
    points = []
    with open(data_path, "r") as file:
        next(file)
        for line in file:
            line = line.strip().split(",")
            if len(line) == 3:
                x, y, label = line
                points.append((float(x), float(y), int(label)))
    return points


# Läs in testpoints (endast x, y)

def load_test_points(test_path):
    points = []
    with open(test_path, "r") as file:
        next(file)
        for line in file:
            line = line.strip()
            line = line.replace("(", "").replace(")", "")
            if line:
                x, y = line.split(",")
                points.append((float(x), float(y)))
    return points

def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def classify_1nn(point, data):
    closest = min(data, key=lambda d: distance(point, (d[0], d[1])))
    return closest[2]

def classify_knn(point, data, k=10):
    sorted_points = sorted(data, key=lambda d: distance(point, (d[0], d[1])))
    k_nearest = sorted_points[:k]
    classes = [p[2] for p in k_nearest]
    majority = Counter(classes).most_common(1)[0][0]
    return majority

def label_to_name(label):
    return "Pichu" if label == 0 else "Pikachu"

# MAIN

if __name__ == "__main__":
    data_points = load_data_points("Labs/datapoints.txt")
    test_points = load_test_points("Labs/testpoints.txt")

    print("=== 1-NN Klassificering ===")
    for tp in test_points:
        result = classify_1nn(tp, data_points)
        print(f"Point {tp} classified as {label_to_name(result)}")

    print("\n=== K-NN (k=10) Klassificering ===")
    for tp in test_points:
        result = classify_knn(tp, data_points, k=10)
        print(f"Point {tp} classified as {label_to_name(result)}")
