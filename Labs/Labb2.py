import matplotlib.pyplot as plt
import numpy as np
import random
from collections import Counter

# Läs in datapoints (width, height, label)

data_path = "Labs/datapoints.txt"
test_path = "Labs/testpoints.txt"

def load_data_points(data_path):
    points = []
    with open(data_path, "r") as file:
        next(file)
        for line in file:
            x, y, label = line.strip().split(",")
            points.append((float(x), float(y), int(label)))
    return points

# Läs in testpoints (endast x, y)

def load_test_points(path):
    points = []
    with open(path, "r") as file:
        next(file)
        for line in file:
            line = line.strip().strip("()")
            x, y = line.split(",")
            points.append((float(x), float(y)))
    return points

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# 1-NN
def classification_1NN(test_point, training_data):
    return min(training_data, key=lambda p: euclidean_distance(test_point, (p[0], p[1])))[2]

# K-NN
def classification_KNN(test_point, training_data, k=10):
    distances = sorted(training_data, key=lambda p: euclidean_distance(test_point, (p[0], p[1])))
    k_nearest = [label for _, _, label in distances[:k]]
    return Counter(k_nearest).most_common(1)[0][0]

# Plotta datapunkter och testresultat
def plot_data(training_data, test_results):
    for x, y, label in training_data:
        plt.scatter(x, y, color="green" if label == 0 else "yellow")
    for x, y, label in test_results:
        plt.scatter(x, y, color="orange" if label == 0 else "blue", marker="x", s=100)

    plt.title("Pikachu vs Pichu")
    plt.xlabel("Width (cm)")
    plt.ylabel("Height (cm)")
    plt.grid(True)
    plt.text(16.5, 40, "Pikachu = Yellow", fontsize=10)
    plt.text(16.5, 39, "Pichu = Green", fontsize=10)
    plt.text(16.5, 38, "Test point identified Pichu = Orange", fontsize=8)
    plt.text(16.5, 37.5, "Test point identified Pikachu = Blue", fontsize=8)
    plt.show()

 # Användarinmatning med felhantering
def user_input_point():
    while True:
        try:
            x = float(input("Ange bredd (cm): "))
            y = float(input("Ange höjd (cm): "))
            if x < 0 or y < 0:
                print ("Värdena måste vara positiva")
                continue
            return (x, y)
        except ValueError:
            print("Ange numeriska värden")

# Slumpad tränings/test-split för accuracy
def compute_accuracy(training_data):
    random.shuffle(training_data)
    train = training_data[:100] # 50 Pikachu, 50 Pichu

    test = training_data[:100:150] # 25 Pikachu, 25 Pichu

    correct = 0
    for x, y, true_label in test:
        pred = classification_KNN((x, y), train, k=10)
        if pred == true_label:
            correct += 1
    accuracy = correct / len(test)
    print(f"Accuracy på testdata: {accuracy:.2f}")

# Huvudprogram
def main():
    training_data = load_data_points(data_path)
    test_points = load_test_points(test_path)

    # Klassificera testpunkter
    test_results = []
    for point in test_points:
        label_knn = classification_KNN(point, training_data, k=10)
        print(f"{point} -> 10-NN: {'Pikachu' if label_knn else 'Pichu'}")
        test_results.append((point[0], point[1], label_knn))

    # Plotta testresultat
    plot_data(training_data, test_results)

    # Användarpunkt
    user_point = user_input_point()
    label_knn_user = classification_KNN(user_point, training_data, k=10)
    print(f"Din testpunkt {user_point} -> 10-NN: {'Pikachu' if label_knn_user else 'Pichu'}")

    # Beräkna enkel accuracy
    compute_accuracy(training_data)

if __name__ == "__main__":
    main()