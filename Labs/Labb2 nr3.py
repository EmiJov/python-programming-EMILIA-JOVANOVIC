import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data_path = "Labs/datapoints.txt"
test_path = "Labs/testpoints.txt"

def load_data_points(data_path):

    points = []

    with open (data_path, "r") as file:
        next(file)
        for line in file:
            x, y, label = line.strip().split(",")
            points.append((float(x), float(y), int(label)))
    return points

def load_test_points(path):

    points = []

    with open(path, "r") as file:
        next(file)

        for line in file:
            line = line.strip().strip("()")

            if line:

                x, y = line.split(",")
                points.append((float(x), float(y)))
    return points
    
def euclidean_distance(p1,p2):
    euclidean_distance = np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    return euclidean_distance

def classification_1NN(test_point, training_data):
    closest_label = None
    minimum_dist = float("inf")
    for x, y, label in training_data:
        d = euclidean_distance(test_point, (x, y))
        if d < minimum_dist:
            minimum_dist = d
            closest_label = label
            return closest_label
        
def plot_data(training_data, test_results):
    for x, y, label in training_data:
        plt.scatter(x, y, color="green" if label == 0 else "yellow")
    for x, y, label in test_results:
        plt.scatter(x, y, color="orange" if label == 0 else "blue") (marker="x", s=100)

    plt.title("Pikachu vs Pichu with 1-NN")
    plt.xlabel("Width (cm)")
    plt.ylabel("Height (cm)")
    plt.grid(True)
    plt.text(16.5, 40, "Pikachu = Yellow", fontsize=10)
    plt.text(16.5, 39, "Pichu = Green", fontsize=10)
    plt.text(16.5, 38, "Test point identified Pichu = Orange", fontsize=8)
    plt.text(16.5, 37.5, "Test point identified Pikachu = Blue", fontsize=8)
    plt.show()

def main ():
    print("Classification of test points:")
    test_results = []

    training_data = load_data_points(data_path)
    test_points = load_test_points(test_path)

    for point in test_points:
        label = classification_1NN(point, training_data)
        label_name = "Pikachu" if label == 1 else "Pichu"
        print(f"Sample with (width, height): {point} classified as {label_name}")
        test_results.append((point[0], point[1], label))

    plot_data(training_data, test_results)

if __name__ == "__main__":
    main()