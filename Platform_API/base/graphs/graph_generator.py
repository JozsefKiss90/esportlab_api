import matplotlib.pyplot as plt
import pandas as pd


def generate_graph(data):
    rts = [item["rt"] for item in data]
    accs = [item["acc"] for item in data]

    plt.bar(rts, accs)
    plt.xlabel("Reaction Time")
    plt.ylabel("Accuracy")
    plt.title("Reaction Time vs Accuracy")
    plt.show()


def generate_graph_from_file(file_path):
    data = pd.read_excel(file_path)
    rts = data["rt"]
    accs = data["acc"]

    plt.bar(rts, accs)
    plt.xlabel("Reaction Time")
    plt.ylabel("Accuracy")
    plt.title("Reaction Time vs Accuracy")
    plt.show()


def generate_graph_from_json(file_path):
    data = pd.read_json(file_path)
    rts = data["rt"]
    accs = data["acc"]

    plt.bar(rts, accs)
    plt.xlabel("Reaction Time")
    plt.ylabel("Accuracy")
    plt.title("Reaction Time vs Accuracy")
    plt.show()

