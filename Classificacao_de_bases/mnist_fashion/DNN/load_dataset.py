import tensorflow as tf
from tensorflow import keras
import numpy as np
import csv

def read_csv(file_path):

    import os

    path = os.getcwd()

    print(path)

    lines = []
    with open(file_path, "r") as file:
        csvreader = csv.reader(file)

        for row in csvreader:
            try:
                lines.append(np.asarray(row, dtype=float))
            except:
                pass
    
    return lines


def load_dataset(dataset_file, width, height):

    loaded_dataset = read_csv(dataset_file)

    m = len(loaded_dataset)
    n = len(loaded_dataset[0])

    x = []
    y = []

    for i in range(0, m):
        y.append(loaded_dataset[i][0])
        x.append([])

        for j in range(1 , n):
            x[-1].append( loaded_dataset[i][j])

    x = np.array(x)
    x /= 255.0

    x = x.reshape((-1, width, height))

    y = np.array(y)

    return x, y

def load_model(json_path, model_path):
    # https://machinelearningmastery.com/save-load-keras-deep-learning-models/
    # load json and create model
    json_file = open(json_path, 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = keras.models.model_from_json(loaded_model_json)

    # load weights into new model
    model.load_weights(model_path)
    return model
